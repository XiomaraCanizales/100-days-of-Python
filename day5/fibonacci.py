def fibonacci(n):
    a = 0
    b = 1

    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

for i in range(10):
  print(fibonacci(i))

my_string = "Hello World"
i = "I"
while i in my_string:
  print(i)