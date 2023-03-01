def fib(n):
	a = 0
	b = 1

	if n == 1:
		print (a)
	else:
		print(a)
		print(b)

		c = a+b
		while c <= n:
			print(c)
			a=b
			b=c
			c = a+b

fib(2)