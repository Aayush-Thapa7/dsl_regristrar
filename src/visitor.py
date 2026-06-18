import sys
import os

# Ensure the grammar folder is in the path to import generated parser files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'grammar')))

try:
    from RegistrarVisitor import RegistrarVisitor
    from RegistrarParser import RegistrarParser
except ImportError:
    print("Warning: ANTLR parser files not found. Please generate them first.")
    class RegistrarVisitor:
        pass
    class RegistrarParser:
        pass

class RegistrarEvalVisitor(RegistrarVisitor):
    def __init__(self, database):
        self.db = database

    def visitEnrollCmd(self, ctx):
        student_id = ctx.ID().getText()
        # Extract strings removing the double quotes
        name = ctx.STRING(0).getText()[1:-1]
        major = ctx.STRING(1).getText()[1:-1]
        
        result = self.db.enroll_student(student_id, name, major)
        print(result)
        return result

    def visitDropCmd(self, ctx):
        student_id = ctx.ID().getText()
        result = self.db.drop_student(student_id)
        print(result)
        return result

    def visitPayCmd(self, ctx):
        student_id = ctx.ID().getText()
        amount = float(ctx.NUMBER().getText())
        result = self.db.pay_fee(student_id, amount)
        print(result)
        return result

    def visitGrantCmd(self, ctx):
        student_id = ctx.ID().getText()
        amount = float(ctx.NUMBER().getText())
        result = self.db.grant_scholarship(student_id, amount)
        print(result)
        return result

    def visitShowCmd(self, ctx):
        if ctx.STUDENT():
            student_id = ctx.ID().getText()
            result = self.db.show_student(student_id)
        elif ctx.STUDENTS():
            result = self.db.show_all_students()
        elif ctx.REVENUE():
            result = self.db.show_revenue()
        else:
            result = "Error: Invalid SHOW command."
        print(result)
        return result

    def visitResetCmd(self, ctx):
        result = self.db.reset()
        print(result)
        return result
