# Task 1: SJF Scheduling for TestCase 1
processes_1 = ['P1', 'P2', 'P3', 'P4', 'P5']
arrival_times_1 = [1, 2, 3, 4, 5]
burst_times_1 = [7, 5, 1, 2, 8]

def sjf(processes, arrival_times, burst_times):
    n = len(processes)
    completion_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n
    is_completed = [False] * n
    current_time = 0
    completed = 0

    while completed < n:
        index = -1
        shortest = float('inf')

        for i in range(n):
            if not is_completed[i] and arrival_times[i] <= current_time and burst_times[i] < shortest:
                shortest = burst_times[i]
                index = i

        if index == -1:
            current_time += 1
        else:
            current_time += burst_times[index]
            completion_times[index] = current_time
            turnaround_times[index] = completion_times[index] - arrival_times[index]
            waiting_times[index] = turnaround_times[index] - burst_times[index]
            is_completed[index] = True
            completed += 1

    print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")
    print("\n")

print("SJF Scheduling for TestCase 1:")
sjf(processes_1, arrival_times_1, burst_times_1)


# 2.

processes_2 = ['P1', 'P2', 'P3', 'P4', 'P5']
arrival_times_2 = [6, 3, 4, 1, 2, 5]
burst_times_2 = [1, 3, 6, 5, 2, 1]

def sjf(processes, arrival_times, burst_times):
    n = len(processes)
    completion_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n
    is_completed = [False] * n
    current_time = 0
    completed = 0

    while completed < n:
        index = -1
        shortest = float('inf')

        for i in range(n):
            if not is_completed[i] and arrival_times[i] <= current_time and burst_times[i] < shortest:
                shortest = burst_times[i]
                index = i

        if index == -1:
            current_time += 1
        else:
            current_time += burst_times[index]
            completion_times[index] = current_time
            turnaround_times[index] = completion_times[index] - arrival_times[index]
            waiting_times[index] = turnaround_times[index] - burst_times[index]
            is_completed[index] = True
            completed += 1

    print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")
    print("\n")

print("SJF Scheduling for TestCase 2:")
sjf(processes_2, arrival_times_2, burst_times_2)
