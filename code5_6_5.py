def int_input(text):
    return int(input(text))

def calc_payment(many, menber):
    dnum = many/menber
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = int(pay + 100)
    x = many - pay * (menber - 1)


amount = int(input("支払総額を入れてください"))
people = int(input("参加人数を入力してください"))


dnum = amount/people
pay = dnum // 100 * 100
if dnum > pay:
    pay = int(pay + 100)

payorg = amount - pay * (people - 1)

print("支払額")
print(f"1人あたり{pay}円{people-1}、幹事は{payorg}円です")