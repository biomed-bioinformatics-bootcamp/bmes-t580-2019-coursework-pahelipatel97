import datetime


def print_header():
    print('-----------------------------')
    print('      PREGNANCY WHEEL')
    print('-----------------------------')
    print()


def get_LMP_from_user():
    print("When was your last menstrual period (LMP)? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    LMP = datetime.date(year, month, day)
    return LMP


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = this_year - target_date
    return dt.days


def print_gestational_age(days):
    weeks=int(days/7)
    print("Congratulations!!! Your gestational age is {} weeks.".format(-weeks))

def print_estimated_delivery(original_date):
    original_date = datetime.datetime.strptime(str(original_date), "%Y-%m-%d")
    target_date = original_date + datetime.timedelta(days=281)
    target_date2 = target_date.strftime("%Y-%m-%d")
    target_low = original_date + datetime.timedelta(days=268)
    target_low2 = target_low.strftime("%Y-%m-%d")
    target_high = original_date + datetime.timedelta(days=294)
    target_high2 = target_high.strftime("%Y-%m-%d")
    print('Your estimated delivery date is {}, but may fall anywhere between {} and {}!!!!'.format(target_date2, target_low2, target_high2))


def main():
    print_header()
    LMP = get_LMP_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(LMP, today)
    print_gestational_age(number_of_days)
    print_estimated_delivery(LMP)


main()