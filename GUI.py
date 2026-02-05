import tkinter as tk
from tkinter import ttk, messagebox

from InputParser import parse_requests, DiskInput
from executer import run_all

try:
    import matplotlib
    MATPLOTLIB_AVAILABLE = True
except Exception:
    MATPLOTLIB_AVAILABLE = False

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


class DiskGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Disk Scheduling Simulator")
        self.geometry("900x650")

        self._build()

    def _build(self):
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)

        inputs = ttk.LabelFrame(frm, text="Inputs", padding=10)
        inputs.pack(fill="x")

        ttk.Label(inputs, text="Initial Cylinder:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.initial_var = tk.StringVar(value="53")
        ttk.Entry(inputs, textvariable=self.initial_var, width=12).grid(row=0, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(inputs, text="Last Cylinder:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.last_var = tk.StringVar(value="199")
        ttk.Entry(inputs, textvariable=self.last_var, width=12).grid(row=0, column=3, sticky="w", padx=5, pady=5)

        ttk.Label(inputs, text="Direction:").grid(row=0, column=4, sticky="w", padx=5, pady=5)
        self.dir_var = tk.StringVar(value="Right")
        ttk.Combobox(inputs, textvariable=self.dir_var, values=["Right", "Left"], width=10, state="readonly")\
            .grid(row=0, column=5, sticky="w", padx=5, pady=5)

        ttk.Label(inputs, text="Request Sequence (comma-separated):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.req_var = tk.StringVar(value="98, 183, 37, 122, 14, 124, 65, 67")
        ttk.Entry(inputs, textvariable=self.req_var, width=70).grid(row=1, column=1, columnspan=5, sticky="we", padx=5, pady=5)

        btns = ttk.Frame(frm)
        btns.pack(fill="x", pady=(10, 0))

        ttk.Button(btns, text="Run Simulation", command=self.on_run).pack(side="left")
        ttk.Button(btns, text="Clear Output", command=self.on_clear).pack(side="left", padx=8)

        if MATPLOTLIB_AVAILABLE:
            ttk.Button(btns, text="Plot", command=self.on_plot).pack(side="left", padx=8)
        else:
            ttk.Label(btns, text="(Matplotlib not available: plotting disabled)").pack(side="left", padx=8)

        out = ttk.LabelFrame(frm, text="Output", padding=10)
        out.pack(fill="both", expand=True, pady=10)

        self.text = tk.Text(out, wrap="word")
        self.text.pack(fill="both", expand=True)

        # store last results for plotting
        self._last_results = None
        self._last_data = None

    def on_clear(self):
        self.text.delete("1.0", "end")
        self._last_results = None
        self._last_data = None

    def on_run(self):
        try:
            initial = int(self.initial_var.get().strip())
            last_cyl = int(self.last_var.get().strip())
            direction = self.dir_var.get().strip()
            requests = parse_requests(self.req_var.get().strip())

            data = DiskInput(initial=initial, last_cyl=last_cyl, direction=direction, requests=requests)
            results = run_all(data)

            self._last_results = results
            self._last_data = data

            # Print results
            self.text.delete("1.0", "end")
            self.text.insert("end", "=== Disk Scheduling Simulation Results ===\n\n")
            for name, (path, move) in results.items():
                self.text.insert("end", f"{name}\n")
                self.text.insert("end", f"  Seek Sequence: {path}\n")
                self.text.insert("end", f"  Total Seek Time (head movement): {move}\n\n")

            self.text.insert("end", "--- Comparison (Total Seek Time) ---\n")
            sorted_rows = sorted(((name, mv) for name, (_, mv) in results.items()), key=lambda x: x[1])
            for name, mv in sorted_rows:
                self.text.insert("end", f"{name:7s}: {mv}\n")
            best = sorted_rows[0]
            self.text.insert("end", f"\nBest (lowest movement): {best[0]} with {best[1]}\n")

        except Exception as e:
            messagebox.showerror("Input Error", str(e))

    def on_plot(self):
        if not MATPLOTLIB_AVAILABLE:
            messagebox.showinfo("Plotting Unavailable", "Matplotlib is not available.")
            return
        if not self._last_results:
            messagebox.showinfo("No Data", "Run the simulation first.")
            return

        # Plot each algorithm in separate figures (simple and clear)
        for name, (path, move) in self._last_results.items():
            x = list(range(len(path)))
            y = path

            plt.figure()
            plt.plot(x, y, marker='o')
            plt.title(f"{name} - Total Movement: {move}")
            plt.xlabel("Step")
            plt.ylabel("Cylinder")
            plt.grid(True)

        plt.show()
