<>
# apply-experiments.ps1
# Run dry-run for all YAMLs in chaos-experiments/, then optionally apply them.

$experimentsPath = Join-Path -Path $PSScriptRoot -ChildPath 'chaos-experiments'
if (-not (Test-Path $experimentsPath)) {
    Write-Error "Folder not found: $experimentsPath"
    exit 1
}

$files = Get-ChildItem -Path $experimentsPath -Filter '*.yaml' | Sort-Object Name
if ($files.Count -eq 0) {
    Write-Host "No YAML files found in $experimentsPath"
    exit 0
}

Write-Host "Running server-side dry-run for files in $experimentsPath...`n"
$results = @()
foreach ($f in $files) {
    Write-Host "Dry-run: $($f.Name)"
    try {
        kubectl apply --dry-run=server -f $f.FullName 2>&1 | ForEach-Object { $_ }
        $results += @{ File = $f.Name; DryRun = 'OK' }
    } catch {
        Write-Warning "Dry-run failed for $($f.Name): $_"
        $results += @{ File = $f.Name; DryRun = 'FAIL' }
    }
    Write-Host ""
}

Write-Host "Summary:`n"
$results | ForEach-Object { Write-Host ("{0}: {1}" -f $_.File, $_.DryRun) }

$apply = Read-Host "Apply these files to the cluster? (y/N)"
if ($apply -match '^[Yy]') {
    foreach ($f in $files) {
        Write-Host "Applying: $($f.Name)"
        try {
            kubectl apply -f $f.FullName
        } catch {
            Write-Warning "Apply failed for $($f.Name): $_"
        }
    }
    Write-Host "Done. Check resources with: kubectl get all -n chaos-demo"
} else {
    Write-Host "No changes applied. Exiting."
}
