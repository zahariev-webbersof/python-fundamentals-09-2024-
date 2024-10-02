number_of_courses = int(input())
courses_list = []

for _ in range(number_of_courses):
    course_name = input()
    courses_list.append(course_name)

print(courses_list)