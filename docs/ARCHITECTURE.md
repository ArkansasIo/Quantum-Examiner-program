# Architecture

Device -> Adapter -> Calibration -> Observable Extraction -> Quantum State -> Simulator/Examiner -> MySQL -> HTML5 UI.

## UI
Dashboard, Simulator, Examiner, Devices, Data, and Settings menus.

## Scaling
State-vector simulation requires O(2^N) memory. The browser UI is intentionally lightweight; larger experiments should run in the Python/Rust backend.

## iOS
The frontend is a responsive HTML5 application and can run in iOS Safari. Direct hardware access depends on browser APIs; a network gateway can be used when required.

## Scientific validity
Raw voltage/current/frequency measurements must not be labeled as qubit observables without a documented calibration and measurement model. Provenance and uncertainty should accompany every examination.
