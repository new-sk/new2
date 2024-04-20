import random

sum = 0
for i in range(1000):
  sum += (random.randint(-100,100))
print(sum)

menus = ["짜장", "짦뽕", "볶음밥"]

print(random.choice(menus))

random.ch