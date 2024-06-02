grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_set = list(students)
my_set.sort()
one = sum(grades[0]) / len(grades[0])
two = sum(grades[1]) / len(grades[1])
three = sum(grades[2]) / len(grades[2])
four = sum(grades[3]) / len(grades[3])
five = sum(grades[4]) / len(grades[4])
dict = {}
dict = {my_set[0]: one, my_set[1] : two,  my_set[2] : three,  my_set[3] : four,  my_set[4] : five}
print(dict)