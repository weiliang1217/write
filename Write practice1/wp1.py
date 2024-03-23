products = []
while True: #強制進入loop環節；(boolen-> True or fail)
	item = input('商品名稱: ')
	if item == 'q':
		break # 當再商品紀錄: 輸入'q'時，會執行break 離開loop
	price = input('商品價錢: ')
	products.append([item, price])
print(products)
print(products[0][0])
print(products[0][1])
print(products[1][0])
print(products[1][1])

with open('wp1.csv', 'w', encoding = 'utf-8') as file: #1 將'wp1.csv'作為file稱呼，隨著with open結束 file定義也release。 
                                                       #2 encoding = 'utf-8 '將其內容已utf-8編碼類型寫入csv之中，
                                                       # 當然excel內建初始設定非'utf-8'所以繁體中文會呈現???
	file.write('商品,價錢\n')
	for product in products:
		file.write(product[0] + ',' + product[1] + '\n')

with open('wp1.txt', 'w') as file:
	file.write('商品,價錢\n')
	for product in products:
		file.write(product[0] + ',' + product[1] + '\n')
