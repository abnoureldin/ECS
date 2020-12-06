data = {'Baked Beans': 0.99,
		'Biscuits' : 1.20,
		'Sardines': 1.89,
		'Shampoo (Small)' : 2.00,
		'Shampoo (Medium)' : 2.50,
		'Shampoo (Large)' : 3.50}

basket_1 = {'Baked Beans' : 4,
			'Biscuits' : 1}

basket_2 = {'Baked Beans': 2,
			'Biscuits': 1,
			'Sardines' : 2}

basket_3 = {'Shampoo (Large)' : 3,
			'Shampoo (Medium)' : 1,
			'Shampoo (Small)': 2}

"""
OFFERS
Baked Beans: buy 2 get 1 free
Sardines: 25% discount
"""
def basket(basket):
	# calculates subtotal from function
	print("Subtotal: ","%.2f" % subtotal(basket))
	print("Discount: ","%.2f" % (subtotal(basket) - discounted(basket)))
	print("Total: ","%.2f" % discounted(basket))
	return basket

def subtotal(basket):
	d = {}
	for item,qty in basket.items():
		price = data[item]
		d[item]=(qty*price)
	return sum(d.values())

def discounted(basket):
	basket = offers(basket)
	d = {}
	for item,qty in basket.items():
		price = data[item]
		d[item]=(qty*price)
	return sum(d.values())

def baked_beans(purchased, buy=2, free=1):
    pack = buy + free
    buy_packs = purchased // pack
    buy_individual = purchased % pack
    return buy * buy_packs + buy_individual

def shampoo(purchased, buy=3, free=1):
    pack = buy - free
    buy_packs = purchased // pack
    buy_individual = purchased % pack
    return buy_packs + buy_individual


def offers(basket):
	d = {}
	for item,qty in basket.items():
		if item == 'Baked Beans':
			qty = baked_beans(qty)
			d[item] = qty
		elif item == 'Sardines':
			qty = qty*0.75
			d.update({item:qty})
		elif 'Shampoo' in item:
			qty = shampoo(qty)
			d.update({item:qty})
		else:
			d.update({item:qty})		
	return d





print(basket(basket_1),'\n')
print(basket(basket_2),'\n')
print(basket(basket_3))



