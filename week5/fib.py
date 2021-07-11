def fib(n):
	global count
	if n == 0:
		return 0
	elif n == 1:
		return 1

	else:
		if n == 5: #want to see how many times fib(5) is called when evaluating fib(17). Check if it equals 5 and add to count if it does
			count += 1
		return fib(n-1) + fib(n-2)


def main():
	n = 17
	global count
	count = 0
	i = fib(n)
	print(count)

if __name__ == "__main__":
    main()