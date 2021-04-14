cost = float(input("what's the total bill for today, please?\n==> "))
#calculating the tips
tip_18 = float(cost*18) / 100
tip_20 = float(cost*20) / 100
tip_25 = float(cost*25) / 100
#adding the tip to the cost
total_cost_18 = cost + tip_18
total_cost_20 = cost + tip_20
total_cost_25 = cost + tip_25
#output
print("18% tip is ${}, which brings your total to ${}".format("%.2f" % tip_18,"%.2f" % total_cost_18))
print("20% tip is ${}, which brings your total to ${}".format("%.2f" % tip_20,"%.2f" % total_cost_20))
print("25% tip is ${}, which brings your total to ${}".format("%.2f" % tip_20,"%.2f" % total_cost_25))
