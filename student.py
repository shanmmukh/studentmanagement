from db import conn, cursor

# Add student
def add_student(name, age, grade, email):
    cursor.execute("INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)",
                   (name, age, grade, email))
    conn.commit()
    print(f"Student {name} added successfully!")

# View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Search student
def search_student(search_term):
    cursor.execute("SELECT * FROM students WHERE student_id=? OR name LIKE ?", (search_term, f"%{search_term}%"))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Update student
def update_student(student_id, name=None, age=None, grade=None, email=None):
    cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    student = cursor.fetchone()
    if not student:
        print("Student not found!")
        return
    name = name if name else student[1]
    age = age if age else student[2]
    grade = grade if grade else student[3]
    email = email if email else student[4]
    cursor.execute("UPDATE students SET name=?, age=?, grade=?, email=? WHERE student_id=?",
                   (name, age, grade, email, student_id))
    conn.commit()
    print(f"Student {student_id} updated successfully!")

# Delete student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
    conn.commit()
    print(f"Student {student_id} deleted successfully!")
