# coroner cases: 1. Студенты-тёзки с одинаковой успеваемостью.
# 
#

students = [
    {"name": "Василий Пупкин", "sex": "м", "experience": False, "homework": [10, 8, 9, 10, 9], "exam": [10]},
    {"name": "Василий Пупкин", "sex": "м", "experience": False, "homework": [10, 8, 9, 10, 9], "exam": [10]},
    {"name": "Ольга Матвеева", "sex": "ж", "experience": True, "homework": [3, 8, 2, 6, 6], "exam": [7]},
    {"name": "Илона Давыдова", "sex": "ж", "experience": True, "homework": [7, 8, 9, 10, 6], "exam": [9]},
    {"name": "Никанор Андреев", "sex": "м", "experience": False, "homework": [7, 8, 9, 8, 6], "exam": [10]},
    {"name": "Фёдор Конюхов", "sex": "м", "experience": True, "homework": [7, 8, 9, 10, 7], "exam": [4]},
    {"name": "Вика Машкова", "sex": "ж", "experience": False, "homework": [8, 8, 4, 10, 2], "exam": [5]},
    {"name": "Светлана Артемьева", "sex": "ж", "experience": False, "homework": [9, 2, 9, 10, 6], "exam": [8]},
    {"name": "Иван Зайцев", "sex": "м", "experience": True, "homework": [7, 6, 9, 10, 6], "exam": [7]},
    {"name": "Наташа Смирнова", "sex": "ж", "experience": True, "homework": [5, 8, 10, 10, 7], "exam": [9]}
]

print('Список доступных команд:')
print('aa - средняя оценка за домашние задания и за экзамен по всей группе;')
print('as - средняя оценка за домашние задания и за экзамен по группе в разрезе пола;')
print('ae - средняя оценка за домашние задания и за экзамен по группе в разрезе наличия опыта;')
print('bs - определить лучшего студента.')

def read_key():
    command_key = input('Введите команду:')
    if command_key in ['aa', 'as', 'ae',  'bs']:
        return command_key
    else:
        print('Введите корректную команду')

def average_group_grade():
    sum_of_grades = 0
    sum_of_exams = 0
    grades_count = 0
    exam_count = 0
    for i in students:
        grades_count += len(i['homework'])
        exam_count += len(i['exam'])
    for stud in students:
        for grades in stud['homework']:
            sum_of_grades += grades
        for exams in stud['exam']:
            sum_of_exams += exams
    print('Средняя оценка за домашние задания:', sum_of_grades / grades_count, ', за экзамен:', sum_of_exams / exam_count, 'по всей группе.')

def average_group_grade_sex():
    sum_of_grades_male = 0
    sum_of_exams_male = 0
    sum_of_grades_female = 0
    sum_of_exams_female = 0
    count_of_grades_male = 0
    count_of_grades_female = 0
    count_of_exams_male = 0
    count_of_exams_female = 0
    for stud in students:
        if stud['sex'] == 'м':
            for grades in stud['homework']:
                sum_of_grades_male += grades
                count_of_grades_male += 1
            for exams in stud['exam']:
                sum_of_exams_male += exams
                count_of_exams_male += 1
        elif stud['sex'] == 'ж':
            for grades in stud['homework']:
                sum_of_grades_female += grades
                count_of_grades_female += 1
            for exams in stud['exam']:
                sum_of_exams_female += exams
                count_of_exams_female += 1
    print('Средняя оценка за домашние задания у мужчин:', sum_of_grades_male / count_of_grades_male)
    print('Средняя оценка за экзамен у мужчин:', sum_of_exams_male / count_of_exams_male)
    print('Средняя оценка за домашние задания у женщин:', sum_of_grades_female / count_of_grades_female)
    print('Средняя оценка за экзамен у женщин:', sum_of_exams_female / count_of_exams_female)

def average_group_grade_experience():
    sum_of_grades_exp = 0
    sum_of_exams_exp = 0
    sum_of_grades_noexp = 0
    sum_of_exams_noexp = 0
    count_of_grades_exp = 0
    count_of_grades_noexp = 0
    count_of_exams_exp = 0
    count_of_exams_noexp = 0
    for stud in students:
        if stud['experience'] == True:
            for grades in stud['homework']:
                sum_of_grades_exp += grades
                count_of_grades_exp += 1
            for exams in stud['exam']:
                sum_of_exams_exp += exams
                count_of_exams_exp += 1
        elif stud['experience'] == False:
            for grades in stud['homework']:
                sum_of_grades_noexp += grades
                count_of_grades_noexp += 1
            for exams in stud['exam']:
                sum_of_exams_noexp += exams
                count_of_exams_noexp += 1
    print('Средняя оценка за домашние задания у студентов с опытом:', sum_of_grades_exp / count_of_grades_exp)
    print('Средняя оценка за экзамен у студентов с опытом:', sum_of_exams_exp / count_of_exams_exp)
    print('Средняя оценка за домашние задания у студентов без опыта:', sum_of_grades_noexp / count_of_grades_noexp)
    print('Средняя оценка за экзамен у студентов без опыта:', sum_of_exams_noexp / count_of_exams_noexp)

def best_student():
    sum_of_avg_grades = []
    avg_grades = 0
    i = 0
    j = 0
    for stud in students:
        for grades in stud['homework']:
            avg_grades += grades * 0.6
        avg_grades /= len(stud['homework'])
        for exams in stud['exam']:
            avg_grades += exams * 0.4
        sum_of_avg_grades.append(round(avg_grades, 1))
        avg_grades = 0
    max_grade = max(sum_of_avg_grades)
    max_grade_index = [i for i, j in enumerate(sum_of_avg_grades) if j == max_grade]
    best_student_name = []
    for i in max_grade_index:
        best_student_name.append(students[i]['name'])
    if sum_of_avg_grades.count(max_grade) == 1:
        print('Лучший студент:', best_student_name[0],'с интегральной оценкой', max_grade)
    else:
        print('Лучшие студенты:', ', '.join(best_student_name[0:sum_of_avg_grades.count(max_grade)]),'с интегральной оценкой', max_grade)

input_key = read_key()
if input_key == 'aa':
    average_group_grade()
elif input_key == 'as':
    average_group_grade_sex()
elif input_key == 'ae':
    average_group_grade_experience()
elif input_key == 'bs':
    best_student()