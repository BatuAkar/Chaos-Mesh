# Applying experiments without shell

If you cannot run `kubectl` locally, use one of these GUI options to apply the combined YAML:

1) Kubernetes Dashboard
   - Open your cluster's Kubernetes Dashboard.
   - Go to "Create" or "Upload YAML" (usually top-right) and paste the contents of `all-new-experiments-combined.yaml`.
   - Click "Create". Monitor created resources in the `chaos-demo` namespace.

2) Lens (Kubernetes IDE)
   - Open Lens and connect to your cluster.
   - Select the cluster and namespace `chaos-demo`.
   - Use the "+" / "Create resource" option and paste the YAML from `all-new-experiments-combined.yaml`.

3) Rancher or other cluster UI
   - Most UIs provide a YAML editor or workload creation page — paste the combined YAML and create.

Notes and tips:
- Validate the namespace `chaos-demo` exists. If not, change `namespace:` to one that does.
- If your Dashboard refuses multi-resource YAML, split the file into individual manifests (separate by `---`) and create them one-by-one.
- After creating, check chaos resources:

  - In Dashboard: navigate to custom resources -> `StressChaos` / `PodChaos` / `NetworkChaos` in `chaos-demo`.
  - In Lens: view workloads and custom resources.

If you want, I can also generate five separate single-resource files (one per experiment) to make copy-paste easier in limited editors — söyleyin yeter.
