# 2. 
def round_robin_fcfs(processes, arrival_time, burst_time, time_quantum):
    n = len(processes)
    remaining_burst = burst_time[:]
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0
    queue = []
    completed = 0
    idx = 0

    while completed < n:
        while idx < n and arrival_time[idx] <= time:
            queue.append(idx)
            idx += 1
        if not queue:
            time += 1
            continue
        current = queue.pop(0)
        execute_time = min(time_quantum, remaining_burst[current])
        time += execute_time
        remaining_burst[current] -= execute_time
        while idx < n and arrival_time[idx] <= time:
            queue.append(idx)
            idx += 1
        if remaining_burst[current] > 0:
            queue.append(current)
        else:
            completion_time[current] = time
            turnaround_time[current] = completion_time[current] - arrival_time[current]
            waiting_time[current] = turnaround_time[current] - burst_time[current]
            completed += 1

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")

# # 1.
# processes = ["P1", "P2", "P3", "P4", "P5"]
# arrival_time = [1, 2, 3, 4, 5]
# burst_time = [7, 5, 1, 2, 8]
# time_quantum = 3
# round_robin_fcfs(processes, arrival_time, burst_time, time_quantum)

# 2. 
processes = ["P1", "P2", "P3", "P4", "P5"]
arrival_time = [6, 3, 4, 1, 2, 5]
burst_time = [1, 3, 6, 5, 2, 1]
time_quantum = 3
round_robin_fcfs(processes, arrival_time, burst_time, time_quantum)