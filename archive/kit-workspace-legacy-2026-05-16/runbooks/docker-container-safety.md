# Docker / Container Safety

Check:

- trusted and pinned base image
- minimal final image and multi-stage build where useful
- `.dockerignore` excludes secrets and large irrelevant files
- secrets are not baked into layers
- non-root user where practical
- explicit ports, env vars, and healthcheck
- deterministic dependency install
- no unnecessary package managers/tools in final image
