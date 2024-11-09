# 1
user_input = input("word: ")
result_list = list(user_input.lower())
print("Result")
print(result_list)


print("2)")
input_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]
vowels = {'a', 'e', 'i', 'o', 'u'}
list_vow = []
list_cons = []
list_sym = []

for char, count in input_list:
    if char in vowels:
        list_vow.append((char, count))
    elif char.isalpha():
        list_cons.append((char, count))
    else:
        list_sym.append((char, count))

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)

print("2.1")
name = input("Name: ")

assignment_scores = list(map(int, input("scores for assignments: ").split(',')))
lab_scores = list(map(float, input("labs: ").split(',')))
test_scores = list(map(int, input("tests: ").split(',')))

student = {
    'name': name,
    'assignment': assignment_scores,
    'test': test_scores,
    'lab': lab_scores
}

print(student)

print("2.2)")
name = input("name: ")
assignment_scores = list(map(int, input("assigments: ").split(',')))
lab_scores = list(map(float, input("Labs: ").split(',')))
test_scores = list(map(int, input("Test: ").split(',')))

student = {
    'name': name,
    'assignment': assignment_scores,
    'test': test_scores,
    'lab': lab_scores
}

submission_count = len(student['assignment']) + len(student['test']) + len(student['lab'])

submission_check = {student['name']: submission_count}

print(submission_check)

print("2.3)")
name = input("Name: ")

assignment_scores = list(map(int, input("assignment: ").split(',')))
lab_scores = list(map(float, input("labs: ").split(',')))
test_scores = list(map(int, input("test: ").split(',')))

student = {
    'name': name,
    'assignment': assignment_scores,
    'test': test_scores,
    'lab': lab_scores
}

submission_count = len(student['assignment']) + len(student['test']) + len(student['lab'])

submission_check = {student['name']: submission_count}

if submission_count >= 4:
    assignment_average = sum(student['assignment']) / len(student['assignment']) if student['assignment'] else 0
    lab_average = sum(student['lab']) / len(student['lab']) if student['lab'] else 0
    test_average = sum(student['test']) / len(student['test']) if student['test'] else 0

    final_grade = (0.3 * assignment_average) + (0.3 * lab_average) + (0.4 * test_average)
else:
    final_grade = 0

student['final_grade'] = final_grade
print("Student: ", student)
print("Submission: ", submission_check)
print("final:", final_grade)


