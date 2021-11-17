from test import courses # Casos test

### Devuelve una lista de las claves de un diccionario dentro de otro 
### courses => dict
### hexamester => str
def courses_offered(courses, hexamester):
    assert isinstance(courses, dict), "El primer parametro no es un dict"
    assert isinstance(hexamester, str), "El segundo parametro no es un str"

    if hexamester not in courses.keys():    # Si el hex. no esta en los cursos
        return []

    return list(courses[hexamester].keys())

### Devuelve una diccionario con todos los cursos con sus fechas en la ha estado person
### courses => dict
### person => str
def involved(courses, person):
    person_courses = {}     # Diccionario vacio que devolveremos, aqui se guardaran todos lso cursos en los que aparezca la variable person
    for date in courses:    # Por cada fecha miraremos que tiene dentro
        date_courses = []   # Esto es un acumudalor que guarda los cursos por cada fecha
        course_in_date = courses_offered(courses, date) 
        for course in course_in_date:   # Por cada curso dentro de los cursos de las fechas
            if person in list(courses[date][course].values()): # Busca si la persona esta dentro de este diccionario
                if course in date_courses:  # Si el curso ya lo hemos visto
                    continue
                date_courses.append(course) # Añade el curso al acumulador

        if date_courses:    # Si data_courses no esta vacio
            person_courses[date] = date_courses # Los cursos se añaden a la persona

    return person_courses


print(involved(courses, 'Dave') )
# {'feb2012': ['cs101'], 'apr2012': ['cs101', 'cs387']}

print(involved(courses, 'Peter C.')) 
# {'feb2012': ['cs101'], 'apr2012': ['cs262']}

print(involved(courses, 'Dorina') )
# {'jan2044': ['cs001']}