tasks = []
task = input("Enter a task:")
tasks.append(task)

print("Current  tasks:")

for index,task in enumerate(tasks,start=1):
    print(f"{index}.{task}")
