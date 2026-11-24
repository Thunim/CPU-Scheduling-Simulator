"""SJF - Shortest Job First (Non-preemptive)"""


def sjf(processes):

    data = [p.copy() for p in processes]

    time = 0
    completed = 0
    timeline = []

    while completed < len(data):

        # Filters only processes that have arrived by the current clock time and aren't finished
        available = [
            p for p in data
            if p["at"] <= time and "ct" not in p
        ]

        if not available:

            next_time = min(
                p["at"] for p in data if "ct" not in p
            )

            timeline.append(("IDLE", time, next_time))
            time = next_time
            continue

        # Choose the process with the shortest burst time
        p = min(available, key=lambda x: (x["bt"], x["at"], x["pid"]))

        start = time
        p["rt"] = start

        # Runs the chosen process completely without interruption
        time += p["bt"]
        p["ct"] = time

        timeline.append((p["pid"], start, time))

        completed += 1

    return data, timeline
