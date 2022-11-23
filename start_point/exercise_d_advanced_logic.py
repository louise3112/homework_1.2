# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# 2. Print the difference between the largest and smallest value:
counter = 1
for number in numbers:
    if counter == 1:
        smallest_value = number
        largest_value = number
    elif number < smallest_value:
        smallest_value = number
    elif number > largest_value:
        largest_value = number
    counter += 1

print(largest_value - smallest_value)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
counter = 0
for number in numbers:
    if counter > 0 and numbers[counter-1] == 2 and number == 2:
        print(f"True")
    counter += 1

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
counter = 0
section_6to7 = False
total_excl_6to7 = 0

for number in numbers:

    if number == 6:
        section_6to7 = True
    elif numbers[counter - 1] == 7:
        section_6to7 = False

    if section_6to7 == False:
        total_excl_6to7 += number

    counter += 1

print(total_excl_6to7) #2


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
counter = 0
total_excl13 = 0

for number in numbers:
    
    if number != 13 and numbers[counter - 1] != 13:
        total_excl13 += number
    
    counter += 1

print(total_excl13) #32
