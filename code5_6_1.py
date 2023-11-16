def weather():
    print("今日は晴れです")
weather()
def calc_circle_area(r):
    return r*r*3.14
print(calc_circle_area(5))
def nowstr():
    return "18時25分30秒"
print(nowstr())
def nowint():
    return 18 , 25 , 30
time , minit , sec = nowint()
print(f"{time}{minit}{sec}")
def is_leaptear(year):
    if year % 4 == 0:
        return True
    else:
        return False
print(is_leaptear(2000))
print(is_leaptear(2001))