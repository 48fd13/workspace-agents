# Security Review Checklist

Use for explicit security review requests. Findings only unless the user asks for fixes.

## Check

- authentication and authorization gaps
- secret handling and accidental exposure
- user input reaching shell, files, database, or external APIs
- overbroad API responses or sensitive fields
- weak cryptography or randomness
- dependency or configuration risk visible in the reviewed scope

## Rules

- Do not report theoretical risks without evidence in the code/config.
- Scope boundaries must be explicit.
- Ask before expanding into operational or infrastructure review.

## Output

Group findings as High, Medium, or Low. Include risk, exploit path or failure mode, file/line, and smallest safe fix.
