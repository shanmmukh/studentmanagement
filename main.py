from student import add_student, view_students, search_student, update_student, delete_student

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            email = input("Email: ")
            add_student(name, age, grade, email)

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_term = input("Enter Student ID or Name to search: ")
            search_student(search_term)

        elif choice == "4":
            student_id = int(input("Enter Student ID to update: "))
            name = input("New Name (leave blank to keep current): ")
            age_input = input("New Age (leave blank to keep current): ")
            age = int(age_input) if age_input else None
            grade = input("New Grade (leave blank to keep current): ")
            email = input("New Email (leave blank to keep current): ")
            update_student(student_id, name, age, grade, email)

        elif choice == "5":
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
