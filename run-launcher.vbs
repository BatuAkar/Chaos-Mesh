' run-launcher.vbs
'Hidden launcher for Local Experiments GUI. Shows an error if it fails to start.
On Error Resume Next
Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
scriptPath = WScript.ScriptFullName
scriptDir = fso.GetParentFolderName(scriptPath)
launcher = scriptDir & "\local-experiments\launcher.py"

cmd = "pythonw " & Chr(34) & launcher & Chr(34)
ret = WshShell.Run(cmd, 0, False)
If Err.Number <> 0 Then
    MsgBox "Launcher could not be started.\nPlease ensure Python is installed and pythonw.exe is on your PATH.", vbCritical, "Launcher Error"
End If
