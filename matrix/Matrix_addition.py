
#2x3 matrix
A=[
  [1,2,3],
  [4,5,6]
]
B=[
  [1,2,3],
  [4,5,6]
]

#Measures Row and Column
len(A)
len(A[0])


"""Matrix Addition
"""

#Addition for same dimensions row x column
#Addition requires: (1 + 1), (2 + 2), (3 + 3),(4 + 4), (5 + 5), (6 + 6)  
#Hence the loop function 
def add_matrices(A,B):

  if len(A)!=len(B):
    raise ValueError("Element Discrepancy: Matrices must have equal number of rows.")
  if len(A[0])!=len(B[0]):
    raise ValueError("Element Discrepancy: Matrices must have equal number of columns.")
  rowsA=len(A)
  columnsA=len(A[0])
  rowsB=len(B)
  columnsB=len(B[0])

  #Need to create an empty result matrix of the correct size for reference
  result=[]
  
  #Outer Loop: for row iteration
  for i in range(rowsA):
    new_row=[]
    #Inner Loop: for column iteration
    for j in range(columnsA):
      #Add the elements A + B
      sumAB=A[i][j]+B[i][j]
      #Append (Add to the end) to the current row
      new_row.append(sumAB)
    #Append the completed row to the resultant matrix
    result.append(new_row)
    
  return result

cresult=add_matrices(A,B)
print("Matrix A + Matrix B=",cresult)







