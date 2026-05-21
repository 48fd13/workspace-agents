# Kubernetes Manifest Checklist

Check:

- labels/selectors match
- requests/limits are set intentionally
- readiness/liveness/startup probes fit app behavior
- env/config/secrets are referenced safely
- rollout strategy and disruption behavior are acceptable
- service/ingress ports match containers
- securityContext is appropriate
- RBAC is least privilege
- storage and namespace assumptions are explicit
