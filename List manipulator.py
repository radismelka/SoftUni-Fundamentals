import sys
numbers = [int(x) for x in input().split()]

command = input()

while not command == "end":
    current_command = command.split()
    if current_command[0] == "exchange":
        index = int(current_command[1])
        if 0 <= index < len(numbers):
            first_half = numbers[index+1::]
            second_half = numbers[:index+1]
            numbers = first_half + second_half
        else:
            print("Invalid index")
    elif current_command[0] == "max":
        max_number = -sys.maxsize
        index = 0
        if current_command[1] == "odd":
            for el in range(len(numbers)):
                if numbers[el] % 2 == 1:
                    if numbers[el] >= max_number:
                        max_number = numbers[el]
                        index = el
        else:
            for el in range(len(numbers)):
                if numbers[el] % 2 == 0:
                    if numbers[el] >= max_number:
                        max_number = numbers[el]
                        index = el
        if max_number == -sys.maxsize:
            print("No matches")
        else:
            print(index)
    elif current_command[0] == "min":
        min_number = sys.maxsize
        index = 0
        if current_command[1] == "odd":
            for el in range(len(numbers)):
                if numbers[el] % 2 == 1:
                    if numbers[el] <= min_number:
                        min_number = numbers[el]
                        index = el
        else:
            for el in range(len(numbers)):
                if numbers[el] % 2 == 0:
                    if numbers[el] <= min_number:
                        min_number = numbers[el]
                        index = el
        if min_number == sys.maxsize:
            print("No matches")
        else:
            print(index)
    elif current_command[0] == "first":
        count = int(current_command[1])
        even_or_odd = current_command[2]
        result = []
        if count > len(numbers):
            print("Invalid count")
        else:
            if even_or_odd == "odd":
                for num in range(len(numbers)):
                    if numbers[num] % 2 == 1:
                        result.append(numbers[num])
            else:
                for num in range(len(numbers)):
                    if numbers[num] % 2 == 0:
                        if count > 0:
                            result.append(numbers[num])
            print(result[:count])
    elif current_command[0] == "last":
        count = int(current_command[1])
        even_or_odd = current_command[2]
        result = []
        if count > len(numbers):
            print("Invalid count")
        else:
            if even_or_odd == "odd":
                for num in range(len(numbers)):
                    if numbers[num] % 2 == 1:
                        result.append(numbers[num])
            else:
                for num in range(len(numbers)):
                    if numbers[num] % 2 == 0:
                        if count > 0:
                            result.append(numbers[num])
            print(result[-count:]) # TO DO МНОГО ВАЖНО тук брои отзад напред
            # защото по условие на задачата returns the last count even/odd elements
            # example: [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
            # or example: [1, 8, 2, 3, 6, 9] -> "last 2 odd" -> print [3, 9]
    command = input()

print(numbers)
