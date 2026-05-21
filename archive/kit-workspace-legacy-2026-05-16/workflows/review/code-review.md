# Code Review Checklist

Use for explicit code or diff review requests. Findings only unless the user asks for fixes.

## Review scope

- Review only the specified files, diff, or feature area.
- Do not review unrelated code.
- Ground each finding in a concrete file path and line number when possible.

## Check

- correctness bugs
- broken contracts or edge cases
- missing validation or error handling
- test coverage gaps
- convention drift
- confusing or unnecessarily broad changes

## Output

Group findings by severity:

- Critical: bug, data loss, security issue, broken contract
- Suggestion: meaningful improvement or coverage gap
- Nit: minor style/naming/readability issue

For each finding include: issue, why it matters, path/line, smallest fix.

Close with areas checked with no issues.
