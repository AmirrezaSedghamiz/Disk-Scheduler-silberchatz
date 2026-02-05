from InputParser import parse_requests, DiskInput
from executer import run_all


def cli_main() -> None:
    print("Disk Scheduling Algorithms Simulator (CLI)")
    print("Enter inputs in the specified order.\n")

    initial = int(input("1. Initial Cylinder: ").strip())
    last_cyl = int(input("2. Last Cylinder: ").strip())

    dir_raw = input("3. Movement Direction (Right/Left): ").strip().lower()
    direction = "Right" if dir_raw in ("right", "r", "1", "true", "t") else "Left" if dir_raw in ("left", "l", "0", "false", "f") else dir_raw.title()

    req_text = input("4. Request Sequence (comma-separated): ").strip()
    requests = parse_requests(req_text)

    data = DiskInput(initial=initial, last_cyl=last_cyl, direction=direction, requests=requests)

    results = run_all(data)

    print("\n--- Results ---")
    for name, (path, move) in results.items():
        print(f"\n{name}")
        print(f"  Seek Sequence: {path}")
        print(f"  Total Seek Time (head movement): {move}")

    print("\n--- Comparison (Total Seek Time) ---")
    sorted_rows = sorted(((name, move) for name, (_, move) in results.items()), key=lambda x: x[1])
    for name, move in sorted_rows:
        print(f"{name:7s}: {move}")

    best = sorted_rows[0]
    print(f"\nBest (lowest movement): {best[0]} with {best[1]}")
