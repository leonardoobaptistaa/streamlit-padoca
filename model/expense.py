from dataclasses import dataclass, field
from datetime import date


@dataclass
class Expense:
    file: str
    row_index: int
    date: date
    description: str
    origin: str | None
    amount: float
    validated: bool = False

    def date_key(self):
        return self.date.strftime("%Y-%m-%d")

    def to_present(self):
        return {
            "Data": self.date.strftime("%d/%m/%Y"),
            "Lançamento": self.description,
            "Total": self.amount,
            "Validado": self.validated,
            "Planilha": f"{self.file}#{self.row_index}",
        }


@dataclass
class ExpenseReport:
    expenses: list = field(default_factory=list)

    def add(self, expense):
        self.expenses.append(expense)
