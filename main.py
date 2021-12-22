print("Carleton GPA Calculator")

done = False
grades = [] 
weights = []

while done != True:
  grade = input("Please input your grade: ")
  grades.append(float(grade))
  
  weight = input("Please input the weight: ")
  weights.append(float(weight))

  donePrompt = input("Are you finished? ")
  if donePrompt == "yes" or donePrompt == "y":
    done = True

total = 0
for num in range(0, len(weight)):
  if weight[num] == 0.5:
    total += (grades[num])/2
  else:
    total += grades[num]

average = total / len(weight)

print("Your average is ", average)

