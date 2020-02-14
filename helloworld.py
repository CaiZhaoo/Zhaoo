import random
i=random.randint(1,10)
print('Hello World!')
#dir(__builtins__)
temp=input('数字:')
guess=int(temp)
while (guess!=i):
    temp=input('数字:')
    guess=int(temp)
    if guess==i:
        print('1')
    else:
        print('2')
