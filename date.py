def main():
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4, 
        "May": 5, "June": 6, "July": 7, "August": 8, 
        "September": 9, "October": 10, "November": 11, "December": 12
    }
    
    while True:
        try:
            date_input = input("Date: ").strip()
            if "/" in date_input:
                month, day, year = date_input.split('/')

                month = int(month)
                day = int(day)
                year = int(year)

                if month > 12 or day > 31:
                    raise ValueError("Invalid month or day.")
                
                print(f"{year:04}-{month:02}-{day:02}")
                break

            else:
                month_name, day_year = date_input.split(' ', 1)
                day, year = day_year.split(', ')
                
                day = int(day)
                year = int(year)
                
                if month_name in months:
                    month = months[month_name]
                else:
                    raise ValueError("Invalid month name.")
                
                if day > 31:
                    raise ValueError("Invalid day.")
            
                print(f"{year:04}-{month:02}-{day:02}")
                break
        
        except (ValueError, IndexError):
            print("Invalid date. Please try again.")
            
main()
