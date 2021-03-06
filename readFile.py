#      Program 8 - Sum of Numbers - reading file Chapter 6
#
#      03/02/2021
#
#      Patrick Graham
#
#      The purpose of this program is to read the file of numbers into a    #      list, convert the read lines into integers, and add the numbers  #      together to get the total.

file = open('numbers.txt', 'r')
numbers = []
total = 0
for i in range(5):
  #reads the line of the file
  fileNum = file.readline()
  #adds the value of fileNum to the list numbers at element i.
  numbers.append(fileNum)
  #strips the newline character 
  numbers[i] = fileNum.rstrip('\n')
  #numbers are converted to ints
  numbers[i] = int(numbers[i])
  #ints are added to the accumulator total
  total += numbers[i]
  
#the total is printed and the file is closed
file.close()
print("The total is:",total)




