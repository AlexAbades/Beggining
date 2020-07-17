#1
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 2, 7]
]
#2
for row in number_grid:
    print(row)  #We're saying that he prints all the row as we say:
print("")
print("Brake it down it would be:")  #desglosado paso por paso
print(number_grid[0])
print(number_grid[1])
print(number_grid[2])
print(number_grid[3])
print("")
print("")
#If we want to print element by element, we sholuid say:
#3
for row in number_grid: #I think that's beacuse we can get packs of row but not of columns. We can print row 0, row 1 row 2 and row 3. as we see in the expamle right up, in the brake up example, but we can't print columns.
    for col in row:         #so we have to make a loop inside the row, for every element inside the row, print element.
        print(col)
print("Next Exercise")
