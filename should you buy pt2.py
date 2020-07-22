import time
from selenium import webdriver
from xlwt import Workbook
import dominos
from dominos.api import Client

start = time.time()
total_stock = []


def new_data(data):
	total_stock.append(data)


PATH = "C:\Program Files (x86)\chromedriver.exe"  # your path for the chrome web driver
driver = webdriver.Chrome(PATH)  # for chrome

driver.get(
	"https://www.moneycontrol.com/india/stockmarket/stock-deliverables/marketstatistics/indices/bse-500.html")  # bse 500

stock_name = driver.find_elements_by_tag_name("td")  # element name
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
	new_data(data=ip)
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

for stocking in index_name:
	sheet1.write(stocking, 2, "buy")
for stock_sell in index_name_sell:
	sheet1.write(stock_sell, 2, "sell")

stock_save.save("sample.xls")  # enter the name of the file in the quotation marks
driver.quit()
print(time.time() - start)
