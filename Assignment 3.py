def histogram(l):
    frequency_dict = {}
    for num in l:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    pairs = [(num, frequency) for num, frequency in frequency_dict.items()]
    
    sorted_pairs = sorted(pairs, key=lambda x: (x[1], x[0]))
    
    return sorted_pairs

def transcript(coursedetails, studentdetails, grades):
    course_dict = dict(coursedetails)
    student_dict = dict(studentdetails)
    
    student_grades = {}
    for roll, course, grade in grades:
        if roll not in student_grades:
            student_grades[roll] = []
        student_grades[roll].append((course, grade))
    
    result = []
    for roll in sorted(student_grades.keys()):
        name = student_dict[roll]
        grades = sorted(student_grades[roll], key=lambda x: x[0])
        grades_with_names = [(course, course_dict[course], grade) for course, grade in grades]
        result.append((roll, name, grades_with_names))
    
    return result
