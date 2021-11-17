from test import courses # Casos test

def courses_offered(courses, hexamester):
    if hexamester not in courses.keys():    # Si el hex. no esta en los cursos
        return []

    return list(courses[hexamester].keys())

def is_offered(courses, course, hexamester):
    courses_list = courses_offered(courses, hexamester)
    if course not in courses_list:
        return False
        
    return True

print(is_offered(courses, 'cs101', 'apr2012'))
# True
print(is_offered(courses, 'cs003', 'apr2012'))
# False
print(is_offered(courses, 'cs101', 'may2012'))
# KeyError => False