# Terraform Plan Reading

When reviewing a plan:

- summarize create/update/delete/replace counts
- call out replacements and destroys first
- inspect IAM, networking, security groups, storage, DNS, and database changes carefully
- check provider/module version changes
- check state/backend/workspace assumptions
- note cost-impacting resources
- verify variable/default changes
- require explicit approval before apply
