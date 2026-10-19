# Device Adapter SDK

Adapters normalize hardware streams into timestamped samples containing device identity, channel, voltage, current, optional frequency, raw payload, units, and calibration revision.

Supported adapter targets can include CSV, Serial, Web Serial, Web Bluetooth, network sockets, or a custom gateway.

A calibration/ObservableMapper stage must translate measurements into validated observables. It should document gains, offsets, uncertainty, units, and validation experiments.
