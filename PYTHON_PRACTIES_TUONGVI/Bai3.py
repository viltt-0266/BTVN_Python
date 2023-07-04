import datetime

def calculate_annual_leave(start_date):
    current_date = datetime.date.today()
    start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()

    if start_date.year < current_date.year:
        years_of_service = current_date.year - start_date.year
        if years_of_service >= 5:
            return 14.0
        elif years_of_service >= 4:
            return 13.0
        else:
            return 12.0
    else:
        months_of_service = (current_date - start_date).days // 30
        day_of_month = start_date.day
        if day_of_month >= 10:
            return months_of_service * 0.5
        else:
            return months_of_service


def main():
    start_date = input("Ngày vào làm (dd/mm/yyyy): ")
    annual_leave = calculate_annual_leave(start_date)
    print("Số ngày nghỉ phép: ", annual_leave)


main()
