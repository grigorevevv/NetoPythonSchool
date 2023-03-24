from datetime import datetime


now_str = f'{datetime.now()}\n'

print(now_str)


with open('test_write.txt', 'r') as fw:
    fw.write(now_str)

with open('test_append.txt', 'a') as fa:
    fa.write(now_str)
