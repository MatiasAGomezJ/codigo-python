from Problem_Set_3.test import courses # Casos test

def courses_offered(courses, hexamester):
    if hexamester not in courses.keys():    # Si el hex. no esta en los cursos
        return []

    return list(courses[hexamester].keys())

def when_offered(courses, course):
    dates = []
    for date in courses:
        if course in courses_offered(courses, date):
            dates.append(date)
    
    return dates
        


print(when_offered(courses, 'cs101'))
#['apr2012', 'feb2012']
print(when_offered(courses, 'bio893'))
# []