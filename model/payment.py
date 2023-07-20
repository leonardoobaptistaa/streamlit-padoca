from dataclasses import dataclass, field
from datetime import date


@dataclass
class Payment:
    file: str
    row_index: int
    paid_at: date
    description: str
    amount: float
    validated: bool = False

    def date_key(self):
        return self.paid_at.strftime("%Y-%m-%d")

    def to_present(self):
        return {
            "Data pagamento": self.paid_at.strftime("%d/%m/%Y"),
            "Lançamento": self.description,
            "Total": self.amount,
            "Validado": self.validated,
            "Planilha": f"{self.file}#{self.row_index}",
        }


@dataclass
class PaymentReport:
    payments: list = field(default_factory=list)

    def add(self, payment):
        self.payments.append(payment)
