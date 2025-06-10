import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.revenue_list = []

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
        total_e = sum(e.amount for e in self.expenses)
        total_r = sum(self.revenue_list)
        per_total = (total_e/total_r)*100
        print(f"총 지출: {total_e}원\n")
        print(f"현재 총 수익의 {per_total}% 사용하셨습니다.\n")
        if 0 < per_total and per_total <= 40:
            print("절약하는 자세 좋아요!")
            return
        elif 40 < per_total and per_total <= 70:
            print("이번달은 돈을 좀 쓰셨네요. 다음달은 아껴쓰기!\n")
            return
        elif 70 < per_total and per_total <= 100 :
            print("과소비 하셨습니다! 가계부 내역을 되돌아보면서 소비를 줄이세요! \n")
            return
        elif per_total == 0:
            print("아직 가계부를 작성하지 않으셨나요? 이번 달을 되돌아보아요! \n")
        else : 
            print("파산입니다! 허리띠를 졸라매세요\n")
            
            
    def add_revenue(self):
        try:
            revenue=int(input("수입을 써주세요 : "))
            self.revenue_list.append(revenue)
            total_r = sum(self.revenue_list)
            print(f"수입이 추가되었습니다.\n 현재 총 수익은 {total_r} .\n")
            return

        except ValueError:
            print("오류 발생. 다시 써주세요")
            return
