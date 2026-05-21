# Performance Review Checklist

Use for explicit performance analysis requests. Findings only unless the user asks for fixes.

## Check

- N+1 or repeated data fetching
- missing pagination or over-fetching
- expensive work in loops or render paths
- unnecessary recomputation or allocations
- blocking I/O in async paths
- large dependency imports or missing code splitting
- memory leaks or retained listeners/closures

## Rules

- Every finding needs a concrete code reference.
- Quantify impact where possible.
- Avoid micro-optimizations that reduce readability for negligible gain.

## Output

Group findings as High, Medium, or Low. Include problem, impact, file/line, and fix direction.
