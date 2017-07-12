class Order():
    def __init__(self,meat,topping):
        self.meat = meat
        self.topping = topping

print('Welcome to the Taco Shop! May I take your order?')
meat = input('What is your desired taco meat:')
topping = input('What is your desired taco topping:')
print('Ok! Your taco will contain '+meat,'and '+topping,'!')



