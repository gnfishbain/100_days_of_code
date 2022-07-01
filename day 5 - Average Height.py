# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
Total_height = 0
sum_of_heights = 0

# for loop to count the list length and add the heights together
for height in student_heights:
  #count the list length
  Total_height += height

  #add the input heights together
  sum_of_heights = height + sum_of_heights


#calculate the avarge and round it
avarage_heights = round(sum_of_heights / Total_height)

#print answer
print (avarage_heights)



