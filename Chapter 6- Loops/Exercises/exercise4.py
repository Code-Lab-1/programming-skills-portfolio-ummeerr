sandwich_orders = ['Beef' , 'Chicken' , 'Veggi' , 'cheesy']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(" working on your " + current_sandwich + "sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + "sandwich.")    

