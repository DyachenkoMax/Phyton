task = '1+2+3-2+3*3-8/4'
# task = str(input('Введите пример без пробелов '))
task.replace('','')
print(task)
while '*' in task:
    a = task.index("*")
    answer = int(task[a-1]) * int(task[a+1])
    task = task[0:a-1]+str(answer)+task[a+2:]
    print(f'umn eto {task}')

while '/' in task:
    a = task.index("/")
    answer = int(task[a-1]) // int(task[a+1])
    task = task[0:a-1]+str(answer)+task[a+2:]
    print(f'del {task}')

print(task)

# for i in task:
#     sum = task[i]
#     if '+' in task:
#         pol = task.split('+')
#         # answer = int(task[a-1]) + int(task[a+1])
#         # task = task[0:a-1]+str(answer)+task[a+2:]
#         print(f'pol {pol}')
#     if '-' in task:
#         otr = task.split("-")
#         # answer = int(task[a-1]) - int(task[a+1])
#         # task = task[0:a-1]+str(answer)+task[a+2:]
#         print(f'otr {otr}')

# while '-' in task:
#     a = task.index("-")
#     answer = int(task[a-1]) - int(task[a+1])
#     task = task[0:a-1]+str(answer)+task[a+2:]
#     print(f'min{task}')

print(task)


while '-' in task:
    a = task.index("-")
    answer = int(task[a - 1]) - int(task[a + 1])
    task = task[0:a - 1] + str(answer) + task[a + 2:]
    print(f'min+{task}')

if '+' in task:
    parts = task.split('+')
    sum_parts = 0
    for i in parts:
        sum_parts += int(i)
    print(f'sum_parts это {sum_parts}')
