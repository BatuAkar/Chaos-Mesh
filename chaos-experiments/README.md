# Chaos experiments

This folder contains Chaos Mesh experiment YAMLs used to test resilience.

Files added by assistant:

- `13-cpu-stress.yaml` — high CPU load (`StressChaos`).
- `14-memory-stress.yaml` — high memory allocation (`StressChaos`).
- `15-disk-fill.yaml` — fill filesystem space (`StressChaos`).
- `16-pod-kill.yaml` — randomly kill pods (`PodChaos`).
- `17-network-latency.yaml` — add latency/jitter (`NetworkChaos`).

Prerequisites:

- `kubectl` configured to point at a cluster with Chaos Mesh installed.

Quick usage (run from repository root in PowerShell):

```powershell
.\apply-experiments.ps1
```

This script runs a server-side dry-run for each YAML and asks for confirmation
before applying them. Review each file and ensure the `namespace` and
`labelSelectors` match your deployment.
