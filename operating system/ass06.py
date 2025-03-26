# Total system resources
total_resources = [10, 10, 10]  # A, B, C

# Existing processes: Max and Allocated
processes = {
    "P1": {"Max": [3, 2, 2], "Alloc": [1, 1, 1]},
    "P2": {"Max": [1, 2, 1], "Alloc": [1, 0, 2]},
    "P3": {"Max": [2, 2, 3], "Alloc": [0, 1, 2]}
}

# New process (P4) Request & Max
new_process = "P4"
request_P4 = [2, 1, 2]
processes[new_process] = {"Max": request_P4.copy(), "Alloc": request_P4.copy()}

# Step 1: Calculate current allocation totals
allocated_total = [0, 0, 0]
for p in processes:
    alloc = processes[p]["Alloc"]
    for i in range(3):
        allocated_total[i] += alloc[i]

# Step 2: Calculate Available Resources
available = [total_resources[i] - allocated_total[i] for i in range(3)]

print("Available Resources After Granting Request to P4:", available)

# Step 3: Calculate Needs (Max - Alloc)
needs = {}
for p in processes:
    max_need = processes[p]["Max"]
    alloc = processes[p]["Alloc"]
    needs[p] = [max_need[i] - alloc[i] for i in range(3)]

# Step 4: Safety Algorithm to Check Safe Sequence
def is_safe_state(available, processes, needs):
    work = available.copy()
    finish = {p: False for p in processes}
    safe_sequence = []

    while True:
        allocated_in_this_round = False
        for p in processes:
            if not finish[p]:
                need = needs[p]
                if all(need[i] <= work[i] for i in range(3)):
                    # Can allocate!
                    alloc = processes[p]["Alloc"]
                    for i in range(3):
                        work[i] += alloc[i]
                    finish[p] = True
                    safe_sequence.append(p)
                    allocated_in_this_round = True
        if not allocated_in_this_round:
            break

    if all(finish.values()):
        return True, safe_sequence
    else:
        return False, []

# Step 5: Run Safety Check
safe, sequence = is_safe_state(available, processes, needs)

# Output
if safe:
    print("The system is in a SAFE state.")
    print("Safe sequence is:", " -> ".join(sequence))
else:
    print("The system is in an UNSAFE state.")