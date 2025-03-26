# Suryansh Singh S24MCAG0050
def priority_scheduling(processes, arrival_time, priority, burst_time):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0
    completed = 0
    process_info = list(zip(processes, arrival_time, priority, burst_time))
    process_info.sort(key=lambda x: (x[1], x[2]))

    while completed < n:
        available_processes = [p for p in process_info if p[1] <= time and completion_time[processes.index(p[0])] == 0]
        if not available_processes:
            time += 1
            continue
        current_process = min(available_processes, key=lambda x: x[2])
        idx = processes.index(current_process[0])
        time += current_process[3]
        completion_time[idx] = time
        turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
        waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
        completed += 1
    
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    print("Process\tAT\tPrio\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t{priority[i]}\t{burst_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")

# 1.
processes = ["P1", "P2", "P3", "P4", "P5"]
arrival_time = [1, 2, 3, 4, 5]
priority = [3, 6, 1, 4, 5]
burst_time = [7, 5, 1, 2, 8]
priority_scheduling(processes, arrival_time, priority, burst_time)

# 2. 
processes = ["P1", "P2", "P3", "P4", "P5", "P6"]
arrival_time = [6, 3, 4, 1, 2, 5]
priority = [3, 4, 6, 2, 5, 1]
burst_time = [1, 3, 6, 5, 2, 1]
priority_scheduling(processes, arrival_time, priority, burst_time)