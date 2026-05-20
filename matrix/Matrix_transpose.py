

A = [[1, 2, 3],
     [4, 5, 6]]  #2x3 matrix


#Transpose
rows = len(A) #The len function returns the length of something, Nmber of rows in A = 2
cols = len(A[0]) #row 0 has 3 elements which is the Number of columns in A = 3

#Transposed matrix will have flipped dimensions: (cols x rows) = 3x2
transpose_result = []

for j in range(cols): #Loop through each original column index
    new_row = [] #This column becomes a new row in the transpose
    for i in range(rows): #Loop through each original row index
        new_row.append(A[i][j]) #Take element at row i, col j and place in new row
    transpose_result.append(new_row) #Add the new row to the transposed matrix

print("\nTranspose (A^T):")
for row in transpose_result:
    print(row)
