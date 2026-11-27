"""
CPU Scheduling Simulator
This program simulates varius CPU scheduling algorithms such as determine which process will use the CPU
first. FCFS (First Come, First Served ) executes processes based on their arrival order,
while SJF (Shortest Job First - Non-preemptive) selects the process with the shortest Burst Time and 
allows it to finish without interruption. SRTF (Shortest Remaining Time First - preemptive) executes the 
process with the shortest remaining time and allows interruption when a shorter process arrives. Lastly, 
Preemptive Priority Scheduling (- preemptive) executes the process with the highest priority and interrupts
the current process when a higher-priority process arrives. This program validate data; simulate each algorithm;
create a Gantt chart/timeline; calculate CT, TAT=CT-AT, WT=TAT-BT, RT=first start-AT; compute averages.

Developed by Group 3: (Bezalel Urim O. Siglos, Jolo Majhid C. Mercado, Christian Gerald R. Chavez, )

Files:
    main.py     - menu, input, and result display (run this file)
    fcfs.py     - First Come First Served
    sjf.py      - Shortest Job First (non-preemptive)
    srtf.py     - Shortest Remaining Time First (preemptive)
    priority.py - Priority Scheduling (preemptive)
"""

from fcfs import fcfs
from sjf import sjf
from srtf import srtf
from priority import priority_scheduling


# to get a valid positive integer
def get_number(message, minimum=0):
    while True:
        try:
            number = int(input(message))

            if number < minimum:
                print("Invalid input! Please enter a valid number.")
            else:
                return number

# Prevents the program from crashing if the user types letters instead of numbers
        except ValueError: 
            print("Invalid input! Please enter numbers only.")


# to input processes
def input_processes():

    processes = []

    n = get_number("\nEnter number of processes: ", 1)

    for i in range(n):

        print(f"\nProcess {i + 1}")

        pid = input("Process ID: ").strip()

# Makes sure the Process ID isn't empty and hasn't already been used
        while pid == "" or any(p["pid"] == pid for p in processes):
            print("Invalid or duplicate Process ID!")
            pid = input("Enter another Process ID: ").strip()

        at = get_number("Arrival Time: ")
        bt = get_number("Burst Time: ", 1)
        pr = get_number("Priority: ")

# Stores all details of a single process together as a dictionary
        processes.append({
            "pid": pid,
            "at": at,
            "bt": bt,
            "priority": pr
        })

    return processes


# to print the Gantt chart nicely
def print_gantt_chart(schedule):
    top_bar = "|"
    timeline = str(schedule[0][1])

    for process, start, end in schedule:
        block = f" {process} |"
        top_bar += block

# Calculates exact spaces so ending timestamps align right under each "|" divider
        end_str = str(end)
        spaces_needed = len(block) - len(end_str)
        timeline += (" " * spaces_needed) + end_str

    print("\nGANTT CHART:")
    print(top_bar)
    print(timeline)


# to display Gantt chart and results
def display_results(name, processes, timeline):

    print("\n======================================")
    print("       ", name)
    print("======================================")

    print_gantt_chart(timeline)
    print("\n")

    print("PID\tAT\tBT\tPR\tCT\tTAT\tWT\tRT")

    total_tat = 0
    total_wt = 0
    total_rt = 0

    for p in sorted(processes, key=lambda x: x["pid"]):

# CPU scheduling formulas: Turnaround Time, Waiting Time, and Response Time
        tat = p["ct"] - p["at"]
        wt = tat - p["bt"]
        rt = p["rt"] - p["at"]

        total_tat += tat
        total_wt += wt
        total_rt += rt

        print(
            f'{p["pid"]}\t'
            f'{p["at"]}\t'
            f'{p["bt"]}\t'
            f'{p["priority"]}\t'
            f'{p["ct"]}\t'
            f'{tat}\t'
            f'{wt}\t'
            f'{rt}'
        )

    n = len(processes)

    print("\nAVERAGE RESULTS")
    print("Average TAT:", round(total_tat / n, 2))
    print("Average WT :", round(total_wt / n, 2))
    print("Average RT :", round(total_rt / n, 2))


# MAIN PROGRAM - MENU
def main():

# Maps each menu choice to (display name, algorithm function)
    algorithms = {
        "1": ("FCFS", fcfs),
        "2": ("SJF (NON-PREEMPTIVE)", sjf),
        "3": ("SRTF (PREEMPTIVE)", srtf),
        "4": ("PRIORITY (PREEMPTIVE)", priority_scheduling),
    }

# Main program loop: keeps returning to the menu until the user selects Exit    
    while True:  

        print("\n======================================")
        print("       CPU SCHEDULING SIMULATOR")
        print("======================================")

        print("\nChoose a CPU Scheduling Algorithm:")
        print("[1] FCFS - First Come First Served")
        print("[2] SJF - Shortest Job First")
        print("[3] SRTF - Shortest Remaining Time First")
        print("[4] Priority Scheduling (Preemptive)")
        print("[5] Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using the CPU Scheduling Simulator!")
            break

        if choice not in algorithms:
            print("\nInvalid choice! Please select 1-5.")
            continue

# Get process information
        processes = input_processes()

# Run selected algorithm, then display its results
        name, algorithm = algorithms[choice]
        data, timeline = algorithm(processes)
        display_results(name, data, timeline)


if __name__ == "__main__":
    main()
