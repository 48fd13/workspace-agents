# Observability Instrumentation

Prefer useful, low-noise signals:

- structured logs with request/correlation IDs
- metrics for rate, errors, latency, saturation, and queue depth where relevant
- traces around external calls and important spans
- errors include actionable context without secrets or PII
- metric labels avoid high cardinality
- dashboards/alerts map to user or system impact when applicable
