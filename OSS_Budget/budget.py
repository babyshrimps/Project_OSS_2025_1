import datetime
from expense import Expense

class Budget:
	def __init__(self):
		self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")
        
    def edit_expenses(self):
	    self.list_expenses() 
	    if not self.expenses:
		    return

	    print("수정할 지출 내역을 선택하시오 : ")
	    choose_edit = int(input())
	    
	    if choose_edit < 1 or choose_edit > len(self.expenses):
		    print("잘못입력. 다시 시도하세요.\n")
		    return
		    
	    else :
		    print("수정할 금액을 입력 : ")
		    new_amount = int(input())
		    self.expenses[choose_edit - 1].amount = new_amount
		    print(f"{choose_edit}번 지출 내역의 금액이 {new_amount}원으로 수정.\n")
		    self.total_spent()
