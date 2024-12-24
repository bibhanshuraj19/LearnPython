# Initial setup for the problem

# Process details
processes = {
    "P1": {"group": "G1", "priority": 60, "weight": 0.25},
    "P2": {"group": "G2", "priority": 58, "weight": 0.25},
    "P3": {"group": "G3", "priority": 64, "weight": 0.5},
    "P4": {"group": "G3", "priority": 62, "weight": 0.5},
}

# Group details (weights for each group)
groups = {
    "G1": {"weight": 0.25, "processes": ["P1"]},
    "G2": {"weight": 0.25, "processes": ["P2"]},
    "G3": {"weight": 0.5, "processes": ["P3", "P4"]},
}

# Define the total clock ticks per second
ticks_per_second = 120

# Number of seconds to compute the schedule
total_seconds = 5

# List to store the execution sequence
execution_sequence = []

# Function to determine which process gets executed in each second
def calculate_fair_share_schedule(processes, groups, total_seconds):
    execution_sequence = []

    # Calculate CPU time share for each group (based on weight) per second
    for second in range(1, total_seconds + 1):
        second_schedule = []

        # Loop through each group and assign CPU time based on their weight
        for group, details in groups.items():
            share_ticks = int(details["weight"] * ticks_per_second)
            
            # Distribute the group's share of ticks across its processes
            num_processes = len(details["processes"])
            ticks_per_process = share_ticks // num_processes if num_processes else 0

            for process in details["processes"]:
                second_schedule.append((process, ticks_per_process))

        execution_sequence.append(second_schedule)

    return execution_sequence

# Calculate the fair share execution sequence
schedule = calculate_fair_share_schedule(processes, groups, total_seconds)
schedule
