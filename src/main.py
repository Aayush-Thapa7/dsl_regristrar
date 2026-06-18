import sys
import os
import re
from database import Database

class RegistrarParser:
    def __init__(self, db):
        self.db = db

    def parse_and_execute(self, script_path):
        if not os.path.exists(script_path):
            print(f"Error: File '{script_path}' not found.")
            sys.exit(1)
            
        with open(script_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        print("--- Execution Started ---")
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            
            try:
                self.execute_command(line)
            except Exception as e:
                print(f"Syntax Error at line {line_num}: {line}")
                print(f"Error details: {e}")
                sys.exit(1)
        print("--- Execution Completed ---")

    def execute_command(self, cmd):
        # ENROLL STUDENT 1 NAME "John Doe" MAJOR "Engineering"
        enroll_match = re.match(r'ENROLL\s+STUDENT\s+(\d+)\s+NAME\s+"([^"]+)"\s+MAJOR\s+"([^"]+)"', cmd)
        if enroll_match:
            student_id = enroll_match.group(1)
            name = enroll_match.group(2)
            major = enroll_match.group(3)
            print(self.db.enroll_student(student_id, name, major))
            return

        # DROP STUDENT 1
        drop_match = re.match(r'DROP\s+STUDENT\s+(\d+)', cmd)
        if drop_match:
            student_id = drop_match.group(1)
            print(self.db.drop_student(student_id))
            return

        # PAY FEE 1 AMOUNT 500.00
        pay_match = re.match(r'PAY\s+FEE\s+(\d+)\s+AMOUNT\s+([\d\.]+)', cmd)
        if pay_match:
            student_id = pay_match.group(1)
            amount = float(pay_match.group(2))
            print(self.db.pay_fee(student_id, amount))
            return

        # GRANT SCHOLARSHIP 1 AMOUNT 500.00
        grant_match = re.match(r'GRANT\s+SCHOLARSHIP\s+(\d+)\s+AMOUNT\s+([\d\.]+)', cmd)
        if grant_match:
            student_id = grant_match.group(1)
            amount = float(grant_match.group(2))
            print(self.db.grant_scholarship(student_id, amount))
            return

        # SHOW ALL STUDENTS
        if cmd == 'SHOW ALL STUDENTS':
            print(self.db.show_all_students())
            return

        # SHOW STUDENT 1
        show_student_match = re.match(r'SHOW\s+STUDENT\s+(\d+)', cmd)
        if show_student_match:
            student_id = show_student_match.group(1)
            print(self.db.show_student(student_id))
            return

        # SHOW REVENUE
        if cmd == 'SHOW REVENUE':
            print(self.db.show_revenue())
            return

        # RESET
        if cmd == 'RESET':
            print(self.db.reset())
            return

        raise ValueError(f"Unknown or invalid command format: {cmd}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <script_path.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    db = Database()
    parser = RegistrarParser(db)
    parser.parse_and_execute(input_file)

if __name__ == '__main__':
    main()
