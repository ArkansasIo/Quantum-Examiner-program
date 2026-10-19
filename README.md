# Quantum Examiner Lab

A data-driven quantum simulation and examination platform.

## Goals
- Single-qubit through N-qubit state-vector simulation.
- Bloch-sphere visualization.
- Quantum gates, measurements, tomography, calibration, validation, and experiment logs.
- Responsive HTML5/CSS/JavaScript frontend suitable for iOS Safari.
- Python reference mathematics and simulation engine.
- Rust high-performance core scaffold.
- MySQL persistence and cron-driven analysis jobs.
- Device adapter SDK for electrical measurement streams.
- AutoForm-style data entry.

## Scientific boundary
Electrical sensor data is not automatically a qubit state. A calibrated hardware-to-observable mapping is required before electrical measurements are interpreted as quantum observables.

## Architecture
`Device -> Adapter -> Calibration -> Observable Extraction -> Quantum State -> Simulator/Examiner -> MySQL -> HTML5 UI`

See `docs/` for architecture, API, device adapters, plugins, and feature plans.
