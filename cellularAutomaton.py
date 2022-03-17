
import numpy as np
import math
from matplotlib import pyplot

#############################
# Author: Louis Nguyen
# To use this program, 
# The 1st parameter is a positive integer that specifies the rule number
# The 2nd parameter is a positive integer that specifies the amount of rows you want
# The 3rd parameter is a positive integer that specifies the amount of column's you want
# The 4th parameter is a positive integer between 0-2 inclusive that specifies the styling of the first row,
# 0 is a row of 0's with a 1 in the middle, 1 is a row of 1's with a 0 in the middle, 2 is a random row of 1's and 0's
# The 5th parameter is optional and should only be inputted if the column parameter is even, 
# 'left' if you wish the starting row digit to start left of the middle, 'right' if you wish the starting row digit to start right of the middle
#############################

#Static rules
rules = ['111','110','101','100','011','010','001','000']

#Helper function to determine the next row of matrix
def step(x, binary):
    #convert np array to regular array and expand on both sides
    expanded = np.ndarray.tolist(x)
    expanded.append(expanded[-1])
    expanded.insert(0,expanded[0])

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
    elif cond==3:
        row = [0] * size 
        row[-1] = 1
        return np.array(row)
    elif cond==4:
        row = [0] * size 
        row[0] = 1
        return np.array(row)
    
#Sub function that zooms in on the dimensions we want
def getFrame(matrix, rows,col,lOR,dim):
    #initializes 0 matrix of requested dimensions
    frame = np.zeros((rows, col), dtype=np.int8)
    #setting the offset for if the user specifies if they want left or right starting for even columns
    offset = 0 if lOR=='right' else 1
    
    #if columns are even, then add the offset
    if col%2==0:
        leftBound = (dim//2-1)-(col//2)+1+offset
        rightBound = (dim//2-1)+(col//2)+1+offset
    else:
        #if columns are odd then the value is just in the middle
        leftBound = (dim//2-1)-(col//2)+1
        rightBound = (dim//2-1)+(col//2)+2
    
    #iterate through the frame matrix and set each element equal to the subarray of the overarching matrix
    for i in range(rows):       
        frame[i] = matrix[i][leftBound:rightBound] 
    return frame    
        
#Main function
def cellular_automaton(rule=110, rows=8, col=13, style=0,lOR = 'right'):
    #Checks to make sure that parameters are all valid
    if not isinstance(rule, int) or rule<0 or rule>255:
        raise Exception("Rule number out of bounds")
    if not isinstance(rows, int) or rows<0:
        raise Exception("Invalid Row value")
    if not isinstance(col, int) or col<0:
        raise Exception("Invalid Column value")
    if style<0 or style >3:
        raise Exception("Invalid Style selection")
    if col%2==0 and (not isinstance(lOR, str) or (lOR != 'right' and lOR != 'left')):
        raise Exception("Invalid left or right selection")
    larger = max(col,rows)
    dimension = math.ceil(larger/10)*10 if larger%10!=0 else larger+10
    #Get the binary representation of rule number as a string
    binary = np.binary_repr(rule, width=8) 
    #Convert the binary into an array
    binToArr = np.array([int(digit) for digit in binary])
    #Create a matrix filled with 0's
    matrix = np.zeros((dimension, dimension), dtype=np.int8) 
    #set the first row with appropriate styling
    matrix[0] = firstRow(dimension, style,lOR)
    
    #Iterate through the specified length and call the step function 
    # to generate the rows
    for i in range(len(matrix)-1):
        matrix[i + 1] = step(matrix[i], binToArr)
        
    frame = getFrame(matrix,rows,col,lOR,dimension)
    return frame

# Helper function that generates the plot
def plotDat(data, rule):
    pyplot.figure(figsize=(8,8))
    pyplot.imshow(data)
    pyplot.title(f"Rule: {rule}")
    pyplot.show()
    
# try:
#     rule = int(input("Rule Number?: "))
#     rows = int(input("How many Rows?: "))
#     col = int(input("How many Columns?: "))
#     lOR = 'right'
#     if col%2==0:
#         lOR = input("Columns are even, where would you like the starting index? ('left' for left, 'right' for right): ")

#     style = int(input("What kind of start styling? (0 for a row of 0's with a 1 in the middle, 1 for a row of 1's with a 0 in the middle, 2 for random): "))
# except ValueError:
#     raise Exception("Please enter numbers")

# cellular_automaton(rule,rows,col,style,lOR)
