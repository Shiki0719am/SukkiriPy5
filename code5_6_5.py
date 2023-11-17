def int_input(text):
    return int(input(text))




def calc_payment(many, menber = 2):
    dnum = many/menber
    ans = dnum // 100 * 100
    if dnum > ans:
        ans = int(ans + 100)
    monyorg = many - ans * (menber - 1)
    return int(ans), int(monyorg)

def show_patment(pay,payorg,people = 2):
    print(f"1人あたり{pay}円（{people-1}）人、幹事は{payorg}です")



amount = int(input("支払総額を入れてください"))
people = int(input("参加人数を入力してください"))
pay,payorg = calc_payment(amount,people)
show_patment(pay,payorg,people)