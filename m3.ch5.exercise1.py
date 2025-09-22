num = 0
tot = 0.0
avg = 0.0

while True:
    line = input('Enter a number: ')

    if line == 'done' :
        break

    try:
        fval = float(line)
    except:
        print('Invalid input')
        continue

    num = num + 1
    tot = tot + fval
    avg = tot / num

print('All Done!')
print('Total: ', tot, 'Numbers: ', num, 'Average: ', avg )
