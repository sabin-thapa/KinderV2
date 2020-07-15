import sqlite3
from teacher import Teacher

conn = sqlite3.connect('teacher.db')

c = conn.cursor()

c.execute("""CREATE TABLE teacher (
first text,
last text,
contact integer
)""")

def insert_teacher(tch):
    with conn:
        c.execute("INSERT INTO teacher VALUES (:first, :last, :contact)", {'first': tch.first, 'last': tch.last, 'contact': tch.contact})

def get_teacher_by_name(lastname):
    c.execute("SELECT * FROM teacher WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_contact(tch, contact):
    with conn:
        c.execute("""UPDATE teacher SET contact = :contact
                    WHERE first = :first AND last = :last""",
                    {'first': tch.first, 'last': tch.last, 'contact': contact})


def remove_teacher(tch):
    with conn:
        c.execute("DELETE from teacher WHERE first = :first AND last = :last",
                {'first': tch.first, 'last': tch.last})
teacher_1 = Teacher('ABC','Thapa','98454')
teacher_2 = Teacher('AB','Mahat','968454')

insert_teacher(teacher_1)
insert_teacher(teacher_2)

teacher = get_teacher_by_name('Sabin')
print(teacher)

update_contact(teacher_2, 9845000)
remove_teacher(teacher_1)

teacher = get_teacher_by_name('Sabin')
print(teacher)

conn.close()
