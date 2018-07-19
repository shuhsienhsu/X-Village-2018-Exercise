#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
url = 'http://markets.financialcontent.com/stocks/action/gethistoricaldata?Month=12&Symbol=GOOG&Range=300&Year=2017'
google_stock = pd.read_csv(url)
new_google_stock = google_stock.iloc[::-1] # 因為收到的資料是從 12/29/17 開始到 03/28/14，因此要轉個方向變成3/28/14到12/29/17。
new_google_stock = new_google_stock[:30] # 為了讓上下間距區域變明顯，我們只看前面30天的資料
y = new_google_stock['Open']
y_high = new_google_stock['High']
y_low = new_google_stock['Low']

plt.figure(figsize=(10, 5))
# TODO: magic!
x = range(0, 30)
plt.plot(x, y, color='teal', linewidth=2.0, linestyle='-')
# TODO: another magic!
plt.fill_between(x, y_low, y_high, color = 'pink', alpha = 0.3)

plt.show()