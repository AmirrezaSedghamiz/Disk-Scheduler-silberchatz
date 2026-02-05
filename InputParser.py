from dataclasses import dataclass
from typing import List


@dataclass
class DiskInput:
    initial: int
    last_cyl: int
    direction: str
    requests: List[int]


def validate_inputs(data: DiskInput) -> None:
    if data.last_cyl < 0:
        raise ValueError("Last Cylinder must be >= 0.")
    if not (0 <= data.initial <= data.last_cyl):
        raise ValueError("Initial Cylinder must be within [0, Last Cylinder].")
    if data.direction not in ("Right", "Left"):
        raise ValueError('Direction must be "Right" or "Left".')
    if not data.requests:
        raise ValueError("Request sequence cannot be empty.")
    for r in data.requests:
        if not (0 <= r <= data.last_cyl):
            raise ValueError(f"Request {r} out of range [0, {data.last_cyl}].")


def parse_requests(text: str) -> List[int]:
    parts = [p.strip() for p in text.split(",") if p.strip() != ""]
    if not parts:
        return []
    return [int(p) for p in parts]