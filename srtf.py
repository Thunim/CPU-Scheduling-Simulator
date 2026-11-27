"""SRTF - Shortest Remaining Time First (Preemptive)"""


def srtf(processes):

    data = [p.copy() for p in processes]

    remaining = {p["pid"]: p["bt"] for p in data}

    time = 0
    completed = 0
    timeline = []
    first_start = {}

    while completed < len(data):

        available = [
            p for p in data
            if p["at"] <= time and remaining[p["pid"]] > 0
        ]

        if not available:

            timeline.append(("IDLE", time, time + 1))
            time += 1
            continue

# Select process with shortest remaining time
        p = min(
            available,
            key=lambda x: (remaining[x["pid"]], x["at"], x["pid"])
        )

        pid = p["pid"]

        if pid not in first_start:
            first_start[pid] = time
            p["rt"] = time

# Execute for one time unit (allows switching immediately if a shorter job arrives)
        remaining[pid] -= 1
        time += 1

# Merges consecutive blocks of the same process on the Gantt chart instead of splitting every 1 second
        if timeline and timeline[-1][0] == pid:
            timeline[-1] = (pid, timeline[-1][1], time)
        else:
            timeline.append((pid, time - 1, time))

        if remaining[pid] == 0:
            p["ct"] = time
            completed += 1

    return data, timeline
