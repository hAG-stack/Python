item1_price=34.0
item2_price= 37.5
item3_price= 32.0
total_budget=500
total_cost= item1_price + item2_price + item3_price
print("Total Cost ", total_cost)
print("Total Budget", total_budget)
if total_cost<= total_budget:
    left_money= total_budget - total_cost
    print("Left Money", left_money)
else:
    needed_money= total_cost - total_cost
    print("Needed Money" ,needed_money )