# Network / DNS / TLS Checklist

Check:

- public vs private exposure
- DNS record type, target, TTL, and rollback value
- certificate issuer, SANs, expiration, renewal path
- load balancer/listener/target health behavior
- firewall/security group ports and source ranges
- ingress/path/host routing
- CDN/cache implications
- validation commands or external checks

Ask before live routing, firewall, DNS, or certificate mutations.
