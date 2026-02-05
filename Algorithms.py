from typing import List, Tuple, Dict

def fcfs(initial: int, req: List[int]) -> List[int]:
    return [initial] + req[:]


def sstf(initial: int, req: List[int]) -> List[int]:
    pending = req[:]
    cur = initial
    path = [cur]
    while pending:
        # pick closest (tie-break: smaller cylinder first for determinism)
        pending.sort(key=lambda x: (abs(x - cur), x))
        nxt = pending.pop(0)
        path.append(nxt)
        cur = nxt
    return path


def scan(initial: int, last_cyl: int, direction: str, req: List[int]) -> List[int]:
    left = sorted([r for r in req if r < initial])
    right = sorted([r for r in req if r >= initial])

    path = [initial]
    cur = initial

    if direction == "Right":
        # service right as we go up, then go to end, then reverse and service left descending
        for r in right:
            path.append(r)
            cur = r
        if cur != last_cyl:
            path.append(last_cyl)
            cur = last_cyl
        for r in reversed(left):
            path.append(r)
            cur = r
    else:  # Left
        for r in reversed(left):
            path.append(r)
            cur = r
        if cur != 0:
            path.append(0)
            cur = 0
        for r in right:
            path.append(r)
            cur = r

    return path


def cscan(initial: int, last_cyl: int, direction: str, req: List[int]) -> List[int]:
    left = sorted([r for r in req if r < initial])
    right = sorted([r for r in req if r >= initial])

    path = [initial]
    cur = initial

    if direction == "Right":
        for r in right:
            path.append(r)
            cur = r
        if cur != last_cyl:
            path.append(last_cyl)
            cur = last_cyl
        # jump to start (0) without servicing
        if last_cyl != 0:
            path.append(0)
            cur = 0
        for r in left:
            path.append(r)
            cur = r
    else:  # Left
        for r in reversed(left):
            path.append(r)
            cur = r
        if cur != 0:
            path.append(0)
            cur = 0
        # jump to end without servicing
        path.append(last_cyl)
        cur = last_cyl
        for r in reversed(right):
            path.append(r)
            cur = r

    return path


def look(initial: int, direction: str, req: List[int]) -> List[int]:
    left = sorted([r for r in req if r < initial])
    right = sorted([r for r in req if r >= initial])

    path = [initial]
    cur = initial

    if direction == "Right":
        for r in right:
            path.append(r)
            cur = r
        for r in reversed(left):
            path.append(r)
            cur = r
    else:
        for r in reversed(left):
            path.append(r)
            cur = r
        for r in right:
            path.append(r)
            cur = r

    return path


def clook(initial: int, direction: str, req: List[int]) -> List[int]:
    left = sorted([r for r in req if r < initial])
    right = sorted([r for r in req if r >= initial])

    path = [initial]
    cur = initial

    if direction == "Right":
        for r in right:
            path.append(r)
            cur = r
        if left:
            # jump directly to smallest on left (without servicing in between)
            path.append(left[0])
            cur = left[0]
            for r in left[1:]:
                path.append(r)
                cur = r
    else:  # Left
        for r in reversed(left):
            path.append(r)
            cur = r
        if right:
            # jump directly to largest on right
            path.append(right[-1])
            cur = right[-1]
            for r in reversed(right[:-1]):
                path.append(r)
                cur = r

    return path