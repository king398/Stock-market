from selenium import webdriver
import data
from xlwt import Workbook


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.moneycontrol.com/india/stockmarket/stock-deliverables/marketstatistics/indices/bse-500.html")
stock = driver.find_element_by_tag_name('tbody')
stock_name = driver.find_elements_by_tag_name("td")
chg = []
company_name = []
chosen = []
index_name = []
stock_hold = []
index_name_sell = []
im = -1
rt = -1
for i in stock_name:
	ip = i.text
	data.new_data(data=ip)
	im += 1
	rt += 1
	check = (im - 7) % 10
	check1 = (rt - 4) % 10

	if check == 0:
		chg.append(ip)
	if check1 == 0:
		company_name.append(ip)

print("List index-value are : ")

for index, value in enumerate(chg):
	value_int = float(value)
	index_int = int(index)
	if value_int >= 4:
		print(index_int, "buy")
		chosen.append(value)
		index_name.append(index_int)

	if value_int <= -4:
		print(index_int, "sell")
		chosen.append(value)
		index_name_sell.append(index_int)

stock_save = Workbook()
sheet1 = stock_save.add_sheet('Sheet 1')
sheet_c = 0
for stock_buy in company_name:
	sheet1.write(sheet_c, 0, stock_buy)
	sheet_c += 1
for stocking in index_name:
	sheet1.write(stocking, 1, "buy")
for stock_sell in index_name_sell:
	sheet1.write(stock_sell, 1, "sell")

stock_save.save("sample.xls")
driver.quit()

