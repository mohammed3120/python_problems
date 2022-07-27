import calendar

def get_day_name(string):
    m,d,y  = list(map(int, string.split(' ')))
    n = calendar.weekday(y, m, d)
    dd = calendar.day_name[n].upper()
    return dd

if __name__ == "__main__":
    full_date = input()
    print(get_day_name(full_date))