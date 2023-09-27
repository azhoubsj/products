# 读取档案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,价格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# 让使用者输入
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

# 印出购买记录
for p in products:
	print(p)
	print(p[0], '的价格是', p[1], '元')

# 写入档案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')