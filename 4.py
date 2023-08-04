def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_year(year):
    if leap_year(year):
        return 366
    else:
        return 365

def next_leap_year(year):
    next_year = year + 1
    while not leap_year(next_year):
        next_year += 1
    return next_year

def get_season(month, day):
    seasons = {
        (1, 2, 3): "Winter",
        (4, 5, 6): "Spring",
        (7, 8, 9): "Summer",
        (10, 11, 12): "Fall"
    }
    
    for season_months, season_name in seasons.items():
        if month in season_months:
            return season_name

def main():
    try:
        year = int(input("Enter the year: "))
        month = int(input("Enter the month: "))
        day = int(input("Enter the day: "))
        
        season = get_season(month, day)
        print("Season:", season)
        
        if leap_year(year):
            print(f"{year} is a leap year.")
            days = days_in_year(year)
            print(f"Number of days in {year}: {days}")
        else:
            next_leap = next_leap_year(year)
            print(f"{year} is not a leap year.")
            print(f"Next leap year after {year}: {next_leap}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
