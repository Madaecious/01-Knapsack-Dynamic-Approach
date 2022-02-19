##############################################################################################
# 0/1 Knapsack Problem
# Solution Using Dynamic Approach
# -------------------------------------------------------------
# Mark Barros
# CS3310 - Design and Analysis of Algorithms
# Cal Poly Pomona: Spring 2021
##############################################################################################


# This is an import necessary for reading csv files.
import csv

# This populates the tables.
def populate_tables(profits, weights, tableTwo, numberOfItems, capacity):

    # This initializes the tables with zeros.
    for j in range(0, capacity + 1): 
        tableTwo.append([])
        for i in range(0, numberOfItems + 1):
            tableTwo[j].append(0)

    # This populates the tables with the input values.
    for i in range(0, numberOfItems + 1):
        for j in range(0, capacity + 1):
            if i == 0 or j == 0:
                tableTwo[j][i] = 0
            elif weights[i - 1] <= j:
                tableTwo[j][i] = \
                    max(tableTwo[j][i - 1], \
                    tableTwo[j - weights[i - 1]][i - 1] + profits[i - 1])
            else:
                tableTwo[j][i] = tableTwo[j][i - 1]

# This is the magic part: it finds the right combination.
def optimum(tableOne, weights, n, capacity):
    items = []

    for i in range(0, n):
        tableOne.append(0)

    newCapacity = capacity + 1

    for i in range(n, 0, -1):
        # If upper cell has the lesser value then choose this value.
        if tableTwo[newCapacity - 1][i] > tableTwo[newCapacity - 1][i - 1]:
            tableOne[i - 1] = 1
            newCapacity = newCapacity - weights[i - 1]

    value = tableTwo[capacity][n]

    for i in range(0, n):
        if tableOne[i] == 1:
            items.append(i + 1)

    return value, items

# This is the driver code. ###################################################################

# These will be the tables to be populated.
tableOne = []
tableTwo = []

# These are the necessary variables.
knapsack_capacity = []
numberOfItems = []
item_values = []
item_profits = []
item_weights = []

# This opens the input file as a csv.
input_file = open('input.txt', 'r')
reader = csv.reader(input_file)

# This reads in the values. ------------------------------------
# Note:
# The first line of input.txt is the capacity of the Knapsack
# The second line of is n (number of item types).
# The third line is the weights of the items.
# The fourth line is the value of the items.
for row in reader:
    item_values.append(row)
 
# This maps the values in the input file to the variables.
knapsack_capacity = item_values[0]
knapsack_capacity = list(map(int, knapsack_capacity))
knapsack_capacity = int(knapsack_capacity.pop(0))
numberOfItems = item_values[1]
numberOfItems = list(map(int, numberOfItems))
numberOfItems = int(numberOfItems.pop(0))
item_weights = item_values[2]
item_weights = list(map(int, item_weights))
item_profits = item_values[3]
item_profits = list(map(int, item_profits))

# This populates the tables.
populate_tables( \
    item_weights, \
    item_profits, \
    tableTwo, \
    numberOfItems, \
    knapsack_capacity \
    )

# This outputs the results to the console.
print("----------------------------------------------------------------------------------")
print("0/1 Knapsack Problem - Solution Using Dynamic Approach - By Mark Barros")
print("----------------------------------------------------------------------------------")
print("The results are:")
print()
print("\tMaximum capacity of knapsack: ", knapsack_capacity)
print("\tNumber of items: ", numberOfItems)
print("\tItem Weights: ", *item_weights)
print("\tCorresponding Item Profits: ", *item_profits)
print()
optimum_configuration = \
    optimum(tableOne, item_profits, numberOfItems, knapsack_capacity)
print("Maximum profit and contributions of each item (in order): ", \
    optimum_configuration)
print("----------------------------------------------------------------------------------")
# This is the end of the story. ##############################################################