def process_number(n):
    summary = 0
    for i in n:
        summary += int(i)
    if summary % 2 == 0 and summary * 2 <= 100:
        return f'{summary * 2}'
    elif summary * 3 <= 100:
        return f'{summary * 3}'
    else:
        return 'Превышено'


input_string = input()
result = process_number(input_string)
print(result)