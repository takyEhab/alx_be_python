task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

massage =  " that requires immediate attention today!" if time_bound == "yes" else ". Consider completing it when you have free time."

match priority:
    case "high":
        print(f"Reminder: '{task}' is a {priority} priority task{massage}.")
    case "medium":
        print(f"Reminder: '{task}' is a {priority} priority task{massage}.")        
    case "low":
        print(f"Note: '{task}' is a {priority} priority task{massage}.")        
    case _:
        print("Invalid priority.")
