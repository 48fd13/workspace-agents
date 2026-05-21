# Dependency Review Checklist

Use for dependency, lockfile, package, or license changes.

Check:

- why the dependency is needed
- whether built-in/project code can avoid it
- maintenance status and release recency
- transitive dependency risk
- license compatibility
- security advisories if available
- bundle/runtime impact
- install scripts or postinstall behavior

Ask before installing or mutating dependency state.
