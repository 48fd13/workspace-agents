# Secure Engineering Checklist

Check normal engineering changes for:

- auth/authz and tenant boundaries
- input validation and output encoding
- SQL/NoSQL/command/template injection
- SSRF, path traversal, unsafe redirects
- secrets in code, config, logs, images, or CI
- sensitive data exposure in responses/logs/errors
- unsafe deserialization or file handling
- dependency and supply-chain risk

Keep findings concrete and scoped to reviewed code.
