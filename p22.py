assignment_names = ["Alice", "Bob", "Charlie", "David"]
project_names = []
def check_and_add_to_project(name):
    if name not in assignment_names and name not in project_names:
        project_names.append(name)
        print(f"Added {name} to the project list.")
    else:
        print(f"{name} is already in the assignment list or project list.")

while True:
    student_name = input("Enter the name of the student (or 'exit' to stop): ")
    if student_name.lower() == 'exit':
        break
    check_and_add_to_project(student_name)
print("\nFinal Project List:")
print(project_names)
