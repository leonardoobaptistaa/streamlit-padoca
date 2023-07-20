import math
from datetime import date

from model.expense import Expense, ExpenseReport
from model.payment import Payment, PaymentReport


def dataframe_to_expense_report(df):
    expense_report = ExpenseReport()
    for index, row in df.iterrows():
        expense = datarow_to_expense(index, row, df.name)
        expense_report.add(expense)
    return expense_report


def datarow_to_expense(index, datarow, df_name) -> Expense:
    str_date = datarow["Data"]
    day, month, year = str_date.split("/")
    obj_date = date(int(year), int(month), int(day))

    origin = datarow["Ag. origem"]
    if isinstance(origin, str):
        pass
    elif math.isnan(origin):
        origin = None
    else:
        origin = str(origin)

    return Expense(
        file=df_name,
        row_index=index,
        date=obj_date,
        description=datarow["Lançamento"],
        origin=origin,
        amount=datarow["Valor"],
    )


def dataframes_to_payment_report(dfs):
    payment_report = PaymentReport()
    for df in dfs:
        for index, row in df.iterrows():
            payment = datarow_to_payment(index, row, df.name)
            payment_report.add(payment)
    return payment_report


def datarow_to_payment(index, datarow, df_name) -> Payment:
    str_datetime = datarow["Data"]
    str_date = str_datetime.split(" ")[0]
    year, month, day = str_date.split("-")
    obj_date = date(int(year), int(month), int(day))

    return Payment(
        file=df_name,
        row_index=index,
        paid_at=obj_date,
        description=datarow["Lançamento"],
        amount=datarow["Valor"],
    )
