#This is Exponention **
## You have 1000 Taka ,You invest This money 5 parsent return on Yearly 
#after 10 Years How Much Money ? 
#Your Total Money 1000 Taka. So Yearly 5 Parsent = 1000/100*5
total_money = int(input(" Your Total Money: "))
paresnties = int(input("Give Parsenties on Savings: "))
years = int(input("How Much Time This! 5 or 10: "))
#Calculation
calcualation_one = (total_money/100*paresnties)
#calculation_Two
profit = (calcualation_one*years + total_money)
print(profit)