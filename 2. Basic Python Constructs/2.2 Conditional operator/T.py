first_string = input()
second_string = input()
third_string = input()

search = "зайка"
counter = 0

if search in first_string:
    counter += 1
if search in second_string:
    counter += 1
if search in third_string:
    counter += 1
    
if counter == 1:
    if search in first_string:
        print(first_string, len(first_string))
    elif search in second_string:
        print(second_string, len(second_string))
    else:
        print(third_string, len(third_string))
else:
    min_string = ""
    if (search in first_string):
        min_string = first_string
    if (search in second_string) and (min_string == "" or second_string < min_string):
        min_string = second_string
    if (search in third_string) and (min_string == "" or third_string < min_string):
        min_string = third_string
    print(min_string, len(min_string))