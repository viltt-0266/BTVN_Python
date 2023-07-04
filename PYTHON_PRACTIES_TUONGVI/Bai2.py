def calculate_ot_and_meal_allowance(check_in, check_out):
    try:
        check_in_hour, check_in_minute = map(int, check_in.split(':'))
        check_out_hour, check_out_minute = map(int, check_out.split(':'))

        if check_in_hour < 0 or check_in_hour > 23 or check_in_minute < 0 or check_in_minute > 59 \
                or check_out_hour < 0 or check_out_hour > 23 or check_out_minute < 0 or check_out_minute > 59:
            raise ValueError("Invalid time format")

        total_minutes = (check_out_hour * 60 + check_out_minute) - (check_in_hour * 60 + check_in_minute)
        ot_hours = round(total_minutes / 60, 1)

        lunch = 'N'
        dinner = 'N'

        if ot_hours > 4 and 12 <= check_in_hour < 13:
            ot_hours -= 1
            lunch = 'Y'

        if ot_hours > 3 and check_out_hour >= 21:
            dinner = 'Y'

        return ot_hours, lunch, dinner

    except ValueError as e:
        print(f"Error: {str(e)}")


def main():
    check_in_time = input("Thời gian check-in (hh:mm): ")
    check_out_time = input("Thời gian check-out (hh:mm): ")

    ot_hours, lunch, dinner = calculate_ot_and_meal_allowance(check_in_time, check_out_time)

    if ot_hours is not None:
        print(f"OT: {ot_hours}, Lunch: {lunch}, Dinner: {dinner}")


main()
