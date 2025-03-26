# 1. Objective: Write a Python program to implement the FCFS job scheduling algorithm. Input the number of processes along with their burst durations directly within the code. Calculate and output the Completion time, Turn Around Time, and Waiting Time for each process.
# Input: Number of processes and their respective burst times.
# Output: Calculate and display the Completion time, Turn Around Time, and Waiting Time for each process.
# Example Case:
# Processes: A, B, C, D, E
# Arrival Times: 1, 2, 3, 4, 5
# Burst Times: 5, 2, 3, 4, 50
# Implementation should calculate the waiting and turnaround times as well as the completion time for each process based on the provided data.


# Suryansh Singh (S24MCAG0050)
processes = ['A', 'B', 'C', 'D', 'E']
arrival_times = [1, 2, 3, 4, 5]
burst_times = [5, 2, 3, 4, 50]

# Number of processes
n = len(processes)

# Initialize data structures for storing times
completion_times = [0] * n
turnaround_times = [0] * n
waiting_times = [0] * n

# Sort processes by arrival time (if not already sorted)
process_info = sorted(zip(processes, arrival_times, burst_times), key=lambda x: x[1])
processes, arrival_times, burst_times = zip(*process_info)

# Calculate Completion Time
completion_times[0] = arrival_times[0] + burst_times[0]  # First process completion time
for i in range(1, n):
    # If CPU is idle, it starts at the arrival time of the next process
    completion_times[i] = max(completion_times[i - 1], arrival_times[i]) + burst_times[i]

# Calculate Turnaround Time and Waiting Time
for i in range(n):
    turnaround_times[i] = completion_times[i] - arrival_times[i]
    waiting_times[i] = turnaround_times[i] - burst_times[i]

# Display results
print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
for i in range(n):
    print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")


# 2.
# Objective: This task involves a more complex scenario using the FCFS scheduling algorithm with different arrival and burst times for each process.
# Input: A new set of processes with defined arrival and burst times.
# Output: Similar to Task 1, but with different data to illustrate the FCFS in a different context.
# Example Case:
# Processes: A, B, C, D, E
# Arrival Times: 1, 2, 3, 4, 5
# Burst Times: 50, 4, 3, 2, 5
# Implementation should again calculate the waiting and turnaround times as well as the completion time for each process based on the provided data.


# FCFS Scheduling Algorithm with Different Input Data

# Input: Processes, Arrival Times, and Burst Times
processes = ['A', 'B', 'C', 'D', 'E']
arrival_times = [1, 2, 3, 4, 5]
burst_times = [50, 4, 3, 2, 5]

# Number of processes
n = len(processes)

# Initialize data structures for storing times
completion_times = [0] * n
turnaround_times = [0] * n
waiting_times = [0] * n

# Sort processes by arrival time (if not already sorted)
process_info = sorted(zip(processes, arrival_times, burst_times), key=lambda x: x[1])
processes, arrival_times, burst_times = zip(*process_info)

# Calculate Completion Time
completion_times[0] = arrival_times[0] + burst_times[0]  # First process completion time
for i in range(1, n):
    # If CPU is idle, it starts at the arrival time of the next process
    completion_times[i] = max(completion_times[i - 1], arrival_times[i]) + burst_times[i]

# Calculate Turnaround Time and Waiting Time
for i in range(n):
    turnaround_times[i] = completion_times[i] - arrival_times[i]
    waiting_times[i] = turnaround_times[i] - burst_times[i]

# Display results
print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
for i in range(n):
    print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{completion_times[i]}\t\t{turnaround_times[i]}\t\t{waiting_times[i]}")
