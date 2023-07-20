from collections import defaultdict


class PaymentVerifier:
    def __init__(self, expense_report, payment_report):
        self.expense_report = expense_report
        self.payment_report = payment_report
        self.build_expenses_per_date()

    def build_expenses_per_date(self):
        self.expenses_per_date = defaultdict(list)
        for expense in self.expense_report.expenses:
            self.expenses_per_date[expense.date_key()].append(expense)

    def validate_payments(self):
        for payment in self.payment_report.payments:
            date_expenses = self.expenses_per_date[payment.date_key()]
            for expense in date_expenses:
                match_payment = (
                    abs(expense.amount) == abs(payment.amount)
                    and expense.validated == False
                    and payment.validated == False
                )
                if match_payment:
                    expense.validated = True
                    payment.validated = True
