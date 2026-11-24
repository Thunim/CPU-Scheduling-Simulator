"""FCFS - First Come First Served"""


def fcfs(processes):

    data = [p.copy() for p in processes]

    # Sorts processes strictly by Arrival Time so earliest arrivals run first
    data.sort(key=lambda x: (x["at"], x["pid"]))

    time = 0
    timeline = []

    for p in data:

        # If no process has arrived yet, record CPU IDLE time and jump clock forward
        if time < p["at"]:
            timeline.append(("IDLE", time, p["at"]))
            time = p["at"]

        start = time

        p["rt"] = start
        time += p["bt"]
        p["ct"] = time

        timeline.append((p["pid"], start, time))

    return data, timeline
