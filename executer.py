from typing import List, Tuple, Dict
from Algorithms import fcfs
from Algorithms import sstf
from Algorithms import scan
from Algorithms import cscan
from Algorithms import look
from Algorithms import clook
from InputParser import DiskInput, validate_inputs


def total_movement(path: List[int]) -> int:
    return sum(abs(path[i] - path[i - 1]) for i in range(1, len(path)))


def run_all(data: DiskInput) -> Dict[str, Tuple[List[int], int]]:
    validate_inputs(data)

    algos = {
        "FCFS": lambda: fcfs(data.initial, data.requests),
        "SSTF": lambda: sstf(data.initial, data.requests),
        "SCAN": lambda: scan(data.initial, data.last_cyl, data.direction, data.requests),
        "C-SCAN": lambda: cscan(data.initial, data.last_cyl, data.direction, data.requests),
        "LOOK": lambda: look(data.initial, data.direction, data.requests),
        "C-LOOK": lambda: clook(data.initial, data.direction, data.requests),
    }

    results: Dict[str, Tuple[List[int], int]] = {}
    for name, fn in algos.items():
        path = fn()
        move = total_movement(path)
        results[name] = (path, move)
    return results