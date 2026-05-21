# Cloud Change Safety

Before cloud or infrastructure changes, check:

- target environment and account/project are explicit
- resource names, regions, tags, and ownership are clear
- blast radius is understood
- cost-impacting resources are identified
- security and network exposure changes are called out
- rollback or forward-fix path exists
- validation commands/checks are known
- external mutation requires explicit approval

Never apply, deploy, publish, or mutate shared infrastructure without explicit approval.
