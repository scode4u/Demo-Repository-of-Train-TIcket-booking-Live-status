# Write a Python program to implement SRTF Scheduling. Consider the following input for your reference, and calculate the average waiting time and turnaround time.

# 1.
# processes = ['P1', 'P2', 'P3', 'P4', 'P5']
# arrival_times = [1, 2, 3, 4, 5]
# burst_times = [7, 5, 1, 2, 8]

# 2.
processes = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']
arrival_times = [6, 3, 4, 1, 2, 5]
burst_times = [1, 3, 6, 5, 2, 1]

n = len(processes)
remaining_times = burst_times[:]
completion_times = [0] * n
waiting_times = [0] * n
turnaround_times = [0] * n

current_time = 0
completed = 0
shortest = None
finish_time = 0
min_burst = float('inf')
is_completed = [False] * n

while completed != n:
    for i in range(n):
        if arrival_times[i] <= current_time and not is_completed[i] and remaining_times[i] < min_burst:
            min_burst = remaining_times[i]
            shortest = i
    if shortest is None:
        current_time += 1
        continue
    remaining_times[shortest] -= 1
    min_burst = remaining_times[shortest]
    if min_burst == 0:
        min_burst = float('inf')
    if remaining_times[shortest] == 0:
        completed += 1
        finish_time = current_time + 1
        completion_times[shortest] = finish_time
        turnaround_times[shortest] = completion_times[shortest] - arrival_times[shortest]
        waiting_times[shortest] = turnaround_times[shortest] - burst_times[shortest]
        is_completed[shortest] = True
    current_time += 1

average_waiting_time = sum(waiting_times) / n
average_turnaround_time = sum(turnaround_times) / n

print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
for i in range(n):
    print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")
print(f"Average Waiting Time: {average_waiting_time}")
print(f"Average Turnaround Time: {average_turnaround_time}")