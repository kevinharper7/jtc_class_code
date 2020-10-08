
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()

for i in range(len(meats)):
    meats[i] = meats[i].capitalize()
for i in range(len(cheeses)):
    cheeses[i] = cheeses[i].capitalize()

print(meats)
print(cheeses)
  
print()

print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []

for meat in meats:
    for cheese in cheeses:
	    sandwiches.append(f"{meat} and {cheese}")

print(sandwiches)





print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'

customer_order = input("Can I take your order please?:")

is_on_menu = False
for sandwich in sandwiches:
	if customer_order == sandwich:
		print(f"Great choice 1 {customer_order} coming right up!")
		is_on_menu = True 
if not is_on_menu:
		print(f"Sorry,{customer_order} is not on the menu today")
   


