import matplotlib.pyplot as plt

plt.ion()

def update_pie_chart(data):
    # data[category, price]

    #統整每個分類的金額
    summary = {}
    for category, price in data:
        if category in summary:
            summary[category] += price
        else:
            summary[category] = price

    #清空目前圖表
    plt.clf()

    #畫圓餅圖
    plt.pie(
        summary.values(),
        labels=summary.keys(),
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title("Expense Distribution")
    plt.axis('equal')  # 讓圓變成正圓
    plt.draw()
    plt.pause(0.1)     # 讓畫面更新