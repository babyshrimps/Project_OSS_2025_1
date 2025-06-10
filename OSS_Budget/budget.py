import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, category, description, amount):
	try:
            if date == 't':
                ex_date = datetime.date.today()
            else:
                ex_date = datetime.datetime.strptime(date, '%Y.%m.%d').date()
        except ValueError:
            print("날짜 형식이 올바르지 않음. 'YYYY.MM.DD' 또는 't'로 입력.\n")
            return
        expense = Expense(ex_date, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
	sorted_ex = sorted(self.expenses, key=lambda e: e.date)
        print("\n[지출 목록]")
        for idx, e in enumerate(sorted_ex, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

