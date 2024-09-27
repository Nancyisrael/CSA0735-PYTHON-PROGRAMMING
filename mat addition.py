mat1=[[1,2],[5,3]]
mat2=[[2,3],[4,1]]
result=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):
         result[i][j]=mat1[i][j]+mat2[i][j]
print("resultant matrix")
for col in result:
    print(col)
