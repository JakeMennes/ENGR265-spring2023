## Input all of the Variables
##Cost per Oz of ingredients
wrap_per_oz = 0.47
chicken_per_oz = 0.37
bacon_per_oz = 0.54
shredded_per_oz = 0.38
fries_per_oz = 0.65
cheese_sauce_per_oz = 0.16
funnel_batter_per_oz = 0.63
waffle_batter_per_oz = 0.13
oreo_per_oz = 0.09
marinara_per_oz = 0.34
sticks_per_oz = 0.26

## Popularity as a decimal
LQP = .12
CQP = .11
LBP = .11
MSP = .16
CTP = .15
LFP = .13
FCP = .9
WP = .6
FOP = .7

## Price of each menu thing
LQ_price = 7
CQ_price = 5
LB_price = 10
MS_price = 4
CT_price = 5
LF_price = 7
FC_price = 4
W_price = 8
FO_price = 4

## Total amount of thing sold
Total_Amount_Sold = 100

## Cost of a loaded quesadilla
## Cost Per Oz x the amount of Oz
## Wrap 1, Chicken 3, Bacon 2, Shredded_Cheese 3
Loaded_Quesadilla = ((wrap_per_oz*1)+(chicken_per_oz*3)+(bacon_per_oz*2)+(shredded_per_oz*3))

## Wrap 1, Shredded_Cheese 4
Cheese_Quesadilla = ((wrap_per_oz*1)+(shredded_per_oz*4))

## Wrap 1, Chicken 4, Shredded_Cheese 3, Fries 3, Cheese_Sauce 2, Bacon 2
Burrito_Loaded = ((wrap_per_oz*1)+(chicken_per_oz*4)+(shredded_per_oz*3)+(fries_per_oz*3)+(cheese_sauce_per_oz*2)+(bacon_per_oz*2))

## Sticks 5, Marinara 2
Mozzarella_Sticks = ((sticks_per_oz*5)+(marinara_per_oz*2))

## Chicken 6
Chicken_Tender = (chicken_per_oz*6)

## Fries 5, Cheese_Sauce 3, Bacon 2
Loaded_Fries = ((fries_per_oz*5)+(cheese_sauce_per_oz*3)+(bacon_per_oz*2))

## Funnel_Batter 3
Funnel_Cake = (funnel_batter_per_oz*3)

## Waffle_Batter 6
Waffle = (waffle_batter_per_oz*6)

## Oreo 3, Waffle_Batter 1,
Fried_Oreo = ((oreo_per_oz*4)+(waffle_batter_per_oz*1))

## Amount of each thing Sold
LQA = Total_Amount_Sold * LQP
CQA = Total_Amount_Sold * CQP
LBA = Total_Amount_Sold * LBP
MSA = Total_Amount_Sold * MSP
CTA = Total_Amount_Sold * CTP
LFA = Total_Amount_Sold * LFP
FCA = Total_Amount_Sold * FCP
WA = Total_Amount_Sold * WP
FOA = Total_Amount_Sold * FOP

## Total cost per iteam
LQTC = Loaded_Quesadilla*LQA
CQTC = Cheese_Quesadilla*CQA
LBTC = Burrito_Loaded*LBA
MSTC = Mozzarella_Sticks*MSA
CTTC = Chicken_Tender*CTA
LFTC = Loaded_Fries*LFA
FCTC = Funnel_Cake*FCA
WTC = Waffle*WA
FOTC = Fried_Oreo*FOA

## Total Revenue per iteam
LQTR = LQ_price*LQA
CQTR = CQ_price*CQA
LBTR = LB_price*LBA
MSTR = MS_price*MSA
CTTR = CT_price*CTA
LFTR = LF_price*LFA
FCTR = FC_price*FCA
WTR = W_price*WA
FOTR = FO_price*FOA

## Total cost of selling 500 things
Total_Cost = (LQTC + CQTC + LBTC + MSTC + CTTC + LFTC + FCTC + WTC + FOTC)

## Total Renvenue when selling 500 things
Total_Revenue = (LQTR + CQTR + LBTR + MSTR + CTTR + LFTR + FCTR + WTR + FOTR)

## Total profits
Total_Profit = Total_Revenue - Total_Cost

print("The Total Cost is: " + str(Total_Cost))
print("The Total Revenue is: " + str(Total_Revenue))
print("The Total Profit is: " + str(Total_Profit))

## Margins of all the food iteams
LQM = LQTR/LQTC
CQM = CQTR/CQTC
LBM = LBTR/LBTC
MSM = MSTR/MSTC
CTM = CTTR/CTTC
LFM = LFTR/LFTC
FCM = FCTR/FCTC
WM = WTR/WTC
FOM = FOTR/FOTC

## Margins for iteams
Margin = 0
mylist = (LQM, CQM, LBM, MSM, CTM, LFM, FCM, WM, FOM)
for point in mylist:
    if point > Margin:
        Margin = point
    continue

print("The Largest Margin is for: " + str(Margin))

## Create a graph for the total cost, total profits, total revenue
import matplotlib.pyplot as plt

x = ["Total Profit", "Total Revenue", "Total Cost",]
y = [Total_Profit, Total_Revenue, Total_Cost]

# Create a bar graph
plt.bar(x, y)

# Set the chart title and labels for the x and y axes
plt.title("Total Profit, Total Revenue, Total Cost")
plt.xlabel("TP, TR, TC")
plt.ylabel("Dollars")
# Display the chart
plt.show()

## Create a graph that shows the margins, total coat to make one, and the total revenue for one, for each Menu Iteam.
import matplotlib.pyplot as plt
import numpy as np

# Example data
categories = ["LQ", "CQ", "LB", "MS", "CT", "LF", "FC", "W", "FO"]
set1 = [LQM, CQM, LBM, MSM, CTM, LFM, FCM, WM, FOM]
set2 = [Loaded_Quesadilla, Cheese_Quesadilla, Burrito_Loaded, Mozzarella_Sticks, Chicken_Tender, Loaded_Fries, Funnel_Cake, Waffle, Fried_Oreo]
set3 = [LQ_price, CQ_price, LB_price, MS_price, CT_price, LF_price, FC_price, W_price, FO_price]

# Set the bar width
bar_width = 0.25

# Set the x positions for the bars
x_pos1 = np.arange(len(categories))
x_pos2 = [x + bar_width for x in x_pos1]
x_pos3 = [x + 2 * bar_width for x in x_pos1]

# Create a bar graph with multiple bar groups
plt.bar(x_pos1, set1, width=bar_width, label="Margins")
plt.bar(x_pos2, set2, width=bar_width, label="Cost Per Iteam")
plt.bar(x_pos3, set3, width=bar_width, label="Price Per Iteam")

# Set the chart title and labels for the x and y axes
plt.title("Margins, Price per Iteam, Cost per Iteam")
plt.xlabel("Menu Iteams")
plt.ylabel("Dollars")

# Set the x-axis tick labels
plt.xticks(x_pos2, categories)

# Add a legend to the chart
plt.legend()

# Display the chart
plt.show()


