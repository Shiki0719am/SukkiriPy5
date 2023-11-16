def eat(breakfast, lunch, dinner = "カレー",*desserts):
    print(f"{breakfast}を食べました")
    print(f"{lunch}を食べました")
    print(f"{dinner}を食べました")
    for d in desserts:
        print(f"おやつに{d}を食べました")
eat("トースト", "パスタ", "カレー","アイス","チョコ","パフェ")