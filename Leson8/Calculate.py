loan_amount = float(input("Введите сумму кредита :"))
loan_years = int(input("Введите срок кредита в годах:"))
two_year_proc = 0.02
more_year_proc = 0.04

total_months = loan_years * 12
remainig_loan = loan_amount

print("{:<10} {:<20} {:-<20}".format("Месяц" , "Сумма выплат" , "Проценты"))
print("_" *50)

for month in range(1, total_months + 1):
    if month <= 24:
        interest_rate = two_year_proc
    else:
        interest_rate = more_year_proc

    interest_payment = remainig_loan * interest_rate
    total_payment = remainig_loan + interest_payment

    print("{:<10} , {:<20.2f} , {:<20.2f}" .format(month , total_payment ,interest_payment))

    remainig_loan -= loan_amount / total_months




