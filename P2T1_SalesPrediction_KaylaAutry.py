# A program to predict sales profit.
# 09.12.19
# CTI-110 P1T1 - sales Prediction
#Kayla Autry
#

total_sales = float(input("enter the projected amount of total sales: "))

# calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print("profit=$", format(profit, ',.2f'))
