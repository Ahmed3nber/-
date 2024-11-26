#"Daily Steps Tracker"

input_steps = input("Enter number of steps : ")

steps_split = input_steps.split()

steps = list(map(int, steps_split))

highest_steps = max(steps)
lowest_steps = min(steps)

average_steps = sum(steps) / len(steps)

sorted_steps = sorted(steps, reverse=True)

average_steps_rounded = round(average_steps, 2)


print("\nSteps Analysis: ")
print(f"Highest Steps: {highest_steps}")
print(f"Lowest Steps: {lowest_steps}")
print(f"Average_steps: {average_steps_rounded}")
print(f"Steps Sorted(Highest To Lowest): {sorted_steps}")