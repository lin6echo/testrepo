def new_func():
    age = input("What is your current age?")
    age_as_int = int(age)
    years_remaining = 90 - age_as_int
    days_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    month_remaining = years_remaining * 12

    print(month_remaining)
    print(years_remaining)

    message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {month_remaining} months left."
    print(message)

new_func()
