from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class ElectricalSample:
    timestamp: datetime
    voltage: float
    current: float
    frequency_hz: float | None = None
    channel: str = 'default'
    units: str = 'SI'

class CsvDeviceAdapter:
    def __init__(self, rows):
        self.rows = rows

    def read(self):
        for row in self.rows:
            yield ElectricalSample(
                timestamp=datetime.now(timezone.utc),
                voltage=float(row['voltage']),
                current=float(row['current']),
                frequency_hz=float(row['frequency_hz']) if row.get('frequency_hz') else None,
                channel=row.get('channel','default'))
