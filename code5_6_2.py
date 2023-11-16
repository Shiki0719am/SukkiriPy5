def is_leaptear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False
print(is_leaptear(2000))
print(is_leaptear(1900))
year = int(input("西暦を入力してください"))
if is_leaptear(year) == True:
    print(f"西暦{year}はうるう年です")
else:
    print(f"西暦{year}はうるう年ではありません")
