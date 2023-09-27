products = []
while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break
	price = input('请输入商品价格:')
	# p = []
	# p.append(name)
	# p.append(price) #7-9行等价于p = [name, price]
	products.append([name, price])
print(products)

for p in products:
	print(p)
	print(p[0], '的价格是', p[1], '元')


with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')