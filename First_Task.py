def process_number(n) -> str:
    summary = sum(int(i) for i in n)
    if summary % 2 == 0 and summary * 2 <= 100:
        return str(summary * 2)
    elif summary * 3 <= 100:
        return str(summary * 3)
    else:
        return 'Превышено'


input_string = input()
result = process_number(input_string)
print(result)