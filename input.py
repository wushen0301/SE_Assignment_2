# Input module for expense tracking (Member A)

from output import update_pie_chart

data = []

while True:
    try:
        thing = input("請輸入 分類 金額（例如：food 100）：").split(' ')
        if len(thing) != 2:
            print("格式錯誤，請輸入：分類 金額")
            continue
        category = thing[0]
        price = int(thing[1])
        data.append([category, price])
        update_pie_chart(data)
    except ValueError:
        print("金額必須是數字，請重新輸入")
    except KeyboardInterrupt:
        print("\n程式結束")
        break
