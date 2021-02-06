shark_letters = [letter for letter in 'shark']
print(shark_letters)

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
fish_list = [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)

number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

my_list = [x * y
           for x in [20, 40, 60]
           for y in [2, 4, 6]
           if not x == y*10]
print(my_list)
