
import numpy as np
from matplotlib import pyplot

#Static rules
rules = ['111','110','101','100','011','010','001','000']

#Helper function to determine the next row of matrix
def step(x, binary):
    #convert np array to regular array and expand on both sides
    expanded = np.ndarray.tolist(x)
    expanded.append(0)
    expanded.insert(0, 0)
    
    #Array to return 
    toAdd = []
    
    #Implement a "Sliding window" technique to read concurrent elements of array and
    #Compare to Static rules, if a match then append respective digit to toAdd
    for i in range(0,len(expanded)-2):
        #Empty String
        check = ""
        #Check ahead by 2 digits
        for j in range(i,i+3):
            check+=str(expanded[j])
        #Is the string a static rule? If so add the respective digit to our row array
        if check in rules:
            toAdd.append(binary[rules.index(check)])
        else:
            #Otherwise append 0
            toAdd.append(0)
    #Return the row to add as a numpy array
    return np.array(toAdd)

#Helper function to determine the styling of first row of matrix
def firstRow(size, cond, lOR):
    #If cond is 0 then first row will be a row of 0's with a 1 in the middle
    index = size//2-1 if lOR==0 else size//2
    if cond==0:
        row = [0] * size 
        row[index] = 1
        return np.array(row)
    #If cond is 1 then first row will be a row of 1's with a 0 in the middle
    elif cond == 1:
        row = [1] * size 
        row[index] = 0
        return np.array(row)
    #If cond is 2 than the first row will be a random combo of 1's or 0's
    elif cond == 2:
        return np.random.randint(2, size=size)
    
#Main function
def cellular_automaton(rule=110, rows=8, col=13, style=0,lOR = 0):
    #Checks to make sure that parameters are all valid
    if not isinstance(rule, int) or rule<0 or rule>255:
        raise Exception("Rule number out of bounds")
    if not isinstance(rows, int) or rows<0:
        raise Exception("Invalid Row value")
    if not isinstance(col, int) or col<0:
        raise Exception("Invalid Column value")
    if style<0 or style >2:
        raise Exception("Invalid Style selection")
    
    #Get the binary representation of rule number as a string
    binary = np.binary_repr(rule, width=8) 
    #Convert the binary into an array
    binToArr = np.array([int(digit) for digit in binary])
    #Create a matrix filled with 0's
    matrix = np.zeros((rows, col), dtype=np.int8) 
    #set the first row with appropriate styling
    matrix[0] = firstRow(col, style,lOR)
    
    #Iterate through the specified length and call the step function 
    # to generate the rows
    for i in range(rows - 1):
        matrix[i + 1] = step(matrix[i], binToArr)
    
    plotDat(matrix, rule)
    return matrix

# Helper function that generates the plot
def plotDat(data, rule):
    pyplot.figure(figsize=(8,8))
    pyplot.imshow(data)
    pyplot.title(f"Rule: {rule}")
    pyplot.show()
    
try:
    rule = int(input("Rule Number?: "))
    rows = int(input("How many Rows?: "))
    col = int(input("How many Columns?: "))
    lOR = 0
    if col%2==0:
        lOR = int(input("Columns are even, where would you like the starting index? (0 for left, 1 for right): "))

    style = int(input("What kind of start styling? (0 for a row of 0's with a 1 in the middle, 1 for a row of 1's with a 0 in the middle, 2 for random): "))
except ValueError:
    raise Exception("Please enter numbers")

data = cellular_automaton(rule,rows,col,style,lOR)
plotDat(data, rule)
