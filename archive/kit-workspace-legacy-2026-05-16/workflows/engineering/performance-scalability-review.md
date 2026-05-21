# Performance / Scalability Review

Use for backend/cloud changes that may affect latency, throughput, resource use, or scale.

Check:

- N+1 queries and unbounded loops
- pagination and streaming for large data
- cache correctness and invalidation
- slow DB queries and indexes
- queue throughput and worker concurrency
- retries, timeouts, and connection pools
- memory/CPU limits and large allocations

Avoid micro-optimizations without evidence.
