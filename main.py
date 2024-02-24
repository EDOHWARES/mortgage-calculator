# TODO: 1.

loan_amount = 0

while loan_amount < 1:
    try:
        loan_amount = int(input("Loan amount in dollars: "))
    except ValueError:
        print("loan amount must be a digit!")

    if loan_amount < 1:
        print("loan amount must be a real figure above 1!")

# print(loan_amount)
# print(type(loan_amount))

loan_interest = 0

while loan_interest < 1 or loan_interest > 49:
    try:
        loan_interest = int(input("Loan interest in percentage: "))
    except ValueError:
        print("Loan interest must be a digit!")

    if loan_interest < 1:
        print("Loan interest must be a real figure above 1%!")
    elif loan_interest > 49:
        print("Loan interest cannot be more than 49%")

# print(loan_interest)
# print(type(loan_interest))

duration_of_payment = 0

while duration_of_payment < 1 or duration_of_payment > 30:
    try:
        duration_of_payment = int(input("Duration of payment in years: "))
    except ValueError:
        print("Duration must be inputted in digits!")

    if duration_of_payment < 1 or duration_of_payment > 30:
        print("Duration cannot be less than a year or greater than 30years!")

# print(duration_of_payment)

interest_compound = ""

while interest_compound != "Weekly" and interest_compound != "Monthly" and interest_compound != "Yearly":
    interest_compound = input("Interest compounds, (Weekly, Monthly or Yearly): ").capitalize()

    if interest_compound != "Weekly" and interest_compound != "Monthly" and interest_compound != "Yearly":
        print("Input any of -> Weekly, Monthly or Yearly!")

interest = (loan_interest / 100) * loan_amount
total_payment = loan_amount + interest

print(interest)
print(total_payment)

months_in_duration = duration_of_payment * 12

monthly_payment = loan_amount / months_in_duration

if interest_compound == "Weekly":
    weekly_interest = interest / (4 * months_in_duration)
    monthly_payment = monthly_payment + (weekly_interest * 4)
    r = f"""
Interest per week: ${weekly_interest}
Monthly Payment: ${monthly_payment}
Duration of Payment: {duration_of_payment}yrs
    """
elif interest_compound == "Monthly":
    monthly_interest = interest / months_in_duration
    monthly_payment = monthly_payment + monthly_interest
    r = f"""
Interest per month: ${monthly_interest}
Monthly Payment: ${monthly_payment}
Duration of Payment: {duration_of_payment}yrs
"""
elif interest_compound == "Yearly":
    yearly_interest = interest / duration_of_payment
    monthly_payment = monthly_payment
    r = f"""
Note: You'll pay an interest of ${yearly_interest} at the end of a year
Interest per year: ${yearly_interest}
Monthly Payment: ${monthly_payment}
Duration of payment: {duration_of_payment}yrs
"""


def result():
    return r


if __name__ == "__main__":
    print(result())

