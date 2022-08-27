import sqlite3 as sq
import datetime as dt


def get_timestamp(y, m, d):
    return dt.datetime.timestamp(dt.datetime(y, m, d))


def get_data(tmstmp):
    return dt.datetime.fromtimestamp(tmstmp).date()


courses = [(1, 'python', get_timestamp(2021, 7, 21), get_timestamp(2021, 8, 21)),
           (2, 'java', get_timestamp(2021, 7, 13), get_timestamp(2021, 8, 16))]

students = [(1, 'Max', 'Brooks', 24, 'Spb'),
            (2, 'John', 'Stones', 15, 'Spb'),
            (3, 'Andy', 'Wings', 45, 'Manhester'),
            (4, 'Kate', 'Brooks', 34, 'Spb')]

student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

with sq.connect("brunoyam.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS Students")
    cur.execute("""CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT,
    age INTEGER,
    city TEXT
    )""")

    cur.executemany("INSERT INTO Students VALUES(?, ?, ?, ?, ?)", students)

    cur.execute("DROP TABLE IF EXISTS Courses")
    cur.execute("""CREATE TABLE IF NOT EXISTS Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time_start DATA,
    time_end TEXT
    )""")

    for course in courses:
        cur.execute("INSERT INTO Courses VALUES(?, ?, ?, ?)", course)

    cur.execute("DROP TABLE IF EXISTS Student_courses")
    cur.execute("""CREATE TABLE IF NOT EXISTS Student_courses (
    student_id INTEGER,
    course_id INTEGER
    )""")

    cur.executemany("INSERT INTO Student_courses VALUES(?, ?)", student_courses)

    cur.execute("SELECT name, surname, age FROM Students WHERE age > 30")
    print("Студенты старше 30-ти лет:")
    for student in cur:
        print(*student)

    cur.execute("""SELECT Students.name, Students.surname, Courses.name as course
    FROM Students
    JOIN Student_courses ON Students.id = student_id
    JOIN Courses ON course_id = Courses.id
    WHERE course == 'python'
    """)
    print("========================")
    print("Проходят курс по PYTHON:")
    for student in cur:
        print(student['name'], student['surname'], student['course'])

    cur.execute("""SELECT Students.name, Students.surname, Courses.name as course, Students.city as city
        FROM Students
        JOIN Student_courses ON Students.id = student_id
        JOIN Courses ON course_id = Courses.id
        WHERE course == 'python' and city == 'Spb'
        """)
    print("============================================")
    print("Проходят курс по PYTHON из Санкт-Петербурга:")
    for student in cur:
        print(*student)
