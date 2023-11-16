student_list = ["浅木","松田"]
for student in student_list:
    print(f"{student}さんの試験結果を入力してください")
    network = int(input("ネットワークの得点>>"))
    datebase = int(input("データベースの得点>>"))
    security = int(input("セキュリティの得点>>"))
    if student == "浅木":
        asagi_score = [network, datebase, security]
        asagi_avg = sum(asagi_score)/len(asagi_score)
    else:
        matuda_score = [network, datebase, security]
        matuda_avg = sum(matuda_score)/len(matuda_score)
print(f"浅木さんの平均点は{asagi_avg}です")
print(f"松田さんの平均点は{matuda_avg}です")