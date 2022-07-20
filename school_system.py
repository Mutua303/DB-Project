import csv

from cs50 import SQL
open ('school_system.db','w').close()
database = SQL("sqlite:///school_system.db")
database.execute(""" CREATE TABLE IF NOT EXISTS marks(
    mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    marks INTEGER
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    student_name TEXT,
    group_id INTEGER
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS groups(
    group_id INTEGER PRIMARY KEY,
    group_name TEXT
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS subjects(
    subject_id INTEGER PRIMARY KEY,
    subject_title TEXT
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS teachers(
    teachers_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
    );""")
database.execute(""" CREATE TABLE IF NOT EXISTS relating(
    student_id INTEGER,
    subject_id INTEGER,
    mark_id INTEGER,
    teacher_id INTEGER,
    group_id INTEGER,
    FOREIGN KEY (mark_id) REFERENCES marks(mark_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (student_id)REFERENCES students(student_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers (teachers_id),
    FOREIGN KEY (group_id) REFERENCES groups (group_id)

     );""")



with open ('school_system.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        student_last_name = row['student_last_name']
        group_name = row['group_name']
        teacher_first_name = row['teacher_first_name']
        teacher_last_name = row['teacher_last_name']
        subject_title = row['subject_title']
        date = row['date']
        marks= row['marks']
        
        
        database.execute("INSERT INTO marks(date,marks) VALUES(?,?)",date,marks)
        database.execute("INSERT INTO groups(group_name) VALUES(?)",group_name)
        database.execute("INSERT INTO students(student_name,group_id) VALUES(?,(SELECT group_id FROM groups WHERE group_name = ?))",student_last_name,group_name)
        database.execute("INSERT INTO subjects(subject_title) VALUES(?)",subject_title)
        database.execute("INSERT INTO teachers(first_name,last_name) VALUES(?,?)",teacher_first_name,teacher_last_name)
        database.execute("INSERT INTO relating(mark_id,student_id,subject_id,teacher_id,group_id) VALUES((SELECT mark_id FROM marks WHERE marks =?),(SELECT student_id FROM students WHERE student_name =?),(SELECT subject_id FROM subjects WHERE subject_title = ?),(SELECT teachers_id FROM teachers WHERE first_name = ? ),(SELECT group_id FROM groups WHERE group_name = ?))",marks,student_last_name,subject_title,teacher_first_name,group_name)
        
        
        
        
        