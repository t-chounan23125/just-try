def valid_date(date) :
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sherlock_series = [1887, 1890, 1892, 1894, 1901, 1905, 1915, 1917, 1927]
    splitted = date.split('.')
    year = int(splitted[0])
    month = int(splitted[1])
    day = int(splitted[2])
    is_sherlock_book_yr = lambda x: x in sherlock_series
    if not is_sherlock_book_yr(year):
        print("This is not a publication year of sherlock holmes series.")
    if month < 1 or month > 12:
        print("Invalid month.")
        return False
    if day < 1 or day > days[month - 1]:
        print("Invalid day. ")
        return False

    return True

date = input("Please enter date separately by '.' (e.g., 1917.6.10): ")
if valid_date(date) == True:
    print("This is a publication date of Shersock Holmes!")
else:
    print("This is not a publication date of Sherlock Holmes or you entered it incorrectly.")