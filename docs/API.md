# API Contract

Suggested endpoints:

- GET /health
- GET /api/devices
- POST /api/devices
- POST /api/samples
- POST /api/experiments
- GET /api/experiments/:id
- POST /api/measurements
- POST /api/examinations
- GET /api/examinations/:id
- POST /api/simulations/run

Authentication, TLS, authorization, rate limits, and audit logging are required before exposing the service beyond a trusted development environment.
