import my_module as module
import sys

courses = ["Maths", "Physics", "Computer Science", "Statistics"]

index = module.find_index(courses, "Maths")
print(index)
print(module.name)

print(sys.path)
