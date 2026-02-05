from CLI import cli_main
from GUI import DiskGUI


try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except Exception:
    MATPLOTLIB_AVAILABLE = False


def main():
    print("Choose mode:")
    print("1) CLI")
    print("2) GUI")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        cli_main()
    else:
        app = DiskGUI()
        app.mainloop()


if __name__ == "__main__":
    main()
