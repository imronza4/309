#6010210309 Python3.0
if __name__=="__main__":
  gradelist = []
  for c in range(1,11):
    uslist = input("Enter your grade " + str(c)+": ")
    gradelist.append(uslist)
  print("Before Sorting")
  print(gradelist)
  N = len(gradelist)
  for i in range(1,N):
    for j in range(0,N-i):
            if gradelist[j] > gradelist[j+1] :
                tmp = gradelist[j]
                gradelist[j] = gradelist[j+1]
                gradelist[j+1] = tmp
print("After Sorting ")
print(gradelist)
