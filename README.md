# Disk Scheduling Algorithms Simulator

An Operating Systems course project that simulates and compares classic **disk scheduling algorithms**.  
The program supports both **CLI (Command Line Interface)** and a **GUI (Tkinter)**, allowing users to visualize and compare total disk head movement for different algorithms.

---

## 📚 Course Information
- **Course:** Operating Systems
- **Semester:** Fall 2025
- **Instructor:** Dr. Fakhrahmad
- **Reference:** Silberschatz – *Operating System Concepts*

---

## 🎯 Project Objective
The goal of this project is to:
- Simulate multiple disk scheduling algorithms
- Observe their **seek sequences**
- Calculate and compare **total seek time (head movement)**
- Understand the impact of scheduling strategies on disk performance

---

## 🧠 Algorithms Implemented
The simulator implements the following algorithms:

1. **FCFS (First Come First Serve)**
2. **SSTF (Shortest Seek Time First)**
3. **SCAN**
4. **C-SCAN**
5. **LOOK**
6. **C-LOOK**

---

## 🧾 Input Specifications
The program prompts the user for the following inputs **in order**:

1. **Initial Cylinder**  
   - Starting position of the disk head

2. **Last Cylinder**  
   - Maximum valid cylinder number (disk size, e.g. `199`)

3. **Movement Direction**  
   - `Right` (towards higher cylinder numbers)  
   - `Left` (towards lower cylinder numbers)  
   - Used by SCAN, C-SCAN, LOOK, and C-LOOK

4. **Request Sequence**  
   - Comma-separated list of cylinder requests  
   - Example:  
     ```
     98, 183, 37, 122, 14, 124, 65, 67
     ```

---

## 📤 Output Specifications
For **each algorithm**, the program displays:

- **Seek Sequence** (order of serviced cylinders)
- **Total Seek Time** (total head movement)
- **Comparison** of total seek times across all algorithms

### Bonus
- Optional **graphical visualization** of head movement using matplotlib

---

## 🖥️ How to Run

### 1️⃣ Requirements
- Python **3.8+**
- `tkinter`  
  - Included with Python  
  - On Linux, install with:
    ```bash
    sudo apt install python3-tk
    ```

### 2️⃣ Install Python dependencies
```bash
pip install -r requirements.txt
