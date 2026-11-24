"""Priority Scheduling (Preemptive)"""


def priority_scheduling(processes):

    data = [p.copy() for p in processes]

    remaining = {p["pid"]: p["bt"] for p in data}

    time = 0
    completed = 0
    timeline = []

    while completed < len(data):

        available = [
            p for p in data
            if p["at"] <= time and remaining[p["pid"]] > 0
        ]

        if not available:

            timeline.append(("IDLE", time, time + 1))
            time += 1
            continue

        # Lower priority number means higher priority
        p = min(
            available,
            key=lambda x: (x["priority"], x["at"], x["pid"])
        )

        pid = p["pid"]

        if "rt" not in p:
            p["rt"] = time

        # Runs 1 time unit at a time so a higher-priority arrival can interrupt it
        remaining[pid] -= 1
        time += 1

        # Add process to Gantt chart
        if timeline and timeline[-1][0] == pid:
            timeline[-1] = (pid, timeline[-1][1], time)
        else:
            timeline.append((pid, time - 1, time))

        if remaining[pid] == 0:
            p["ct"] = time
            completed += 1

    return data, timeline
