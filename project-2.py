# created by hussainatphysics@gmail.com(hussainsha syed)

"""
A group of people let say five goes to foreign trip and they also take a oth to donate some percentage of money
over their overall tour expenses
In this project we create calculator that can calculate foreign tour expenses for each person with donation

"""
totalExpenses = int(input("What is the total expense for this foreigh trip \n$"))
but1=input("press enter")

percentageOfdonation = int(input("what percentage of amount would you like to donate? 10, 15, 20?\n"))
but2=input("press enter")
people = int(input("how many people going to this foreign trip?\n"))
but3=input("press enter")
donation = percentageOfdonation/100 * totalExpenses

finalAmount= totalExpenses+donation

amountForEachPerson= finalAmount/people

print(f"The final amount for your foreign trip with donation is :${amountForEachPerson}")
print()
but5=input("press enter for bye!!!!!!!!!!!!!!!!")
