class Database:
    def __init__(self):
        self.students = {}
        self.revenue = 0.0

    def enroll_student(self, student_id, name, major):
        if student_id in self.students:
            return f"Error: Student with ID {student_id} is already enrolled."
        
        self.students[student_id] = {
            'name': name,
            'major': major,
            'balance': 0.0
        }
        return f"Successfully enrolled student: {name} (ID: {student_id}, Major: {major})"

    def drop_student(self, student_id):
        if student_id not in self.students:
            return f"Error: Student with ID {student_id} not found."
        
        name = self.students[student_id]['name']
        del self.students[student_id]
        return f"Successfully dropped student: {name} (ID: {student_id})"

    def pay_fee(self, student_id, amount):
        if student_id not in self.students:
            return f"Error: Student with ID {student_id} not found."
        
        self.students[student_id]['balance'] += amount
        self.revenue += amount
        return f"Payment of ${amount:.2f} received from student ID {student_id}. Current Balance: ${self.students[student_id]['balance']:.2f}"

    def grant_scholarship(self, student_id, amount):
        if student_id not in self.students:
            return f"Error: Student with ID {student_id} not found."
        
        self.students[student_id]['balance'] += amount
        return f"Scholarship of ${amount:.2f} granted to student ID {student_id}. Current Balance: ${self.students[student_id]['balance']:.2f}"

    def show_student(self, student_id):
        if student_id not in self.students:
            return f"Error: Student with ID {student_id} not found."
        
        student = self.students[student_id]
        return f"Student Info:\n  ID: {student_id}\n  Name: {student['name']}\n  Major: {student['major']}\n  Balance: ${student['balance']:.2f}"

    def show_all_students(self):
        if not self.students:
            return "No students enrolled."
        
        res = ["All Enrolled Students:"]
        for sid, info in self.students.items():
            res.append(f"  - {info['name']} (ID: {sid}, Major: {info['major']}, Balance: ${info['balance']:.2f})")
        return "\n".join(res)

    def show_revenue(self):
        return f"Total University Revenue: ${self.revenue:.2f}"

    def reset(self):
        self.students.clear()
        self.revenue = 0.0
        return "Database reset. All student records and revenue cleared."
