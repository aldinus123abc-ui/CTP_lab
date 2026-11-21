class FibonacciGen:
	def __init__(self, terms):
		self.terms = terms
		
	def fibonacci(self, n):
		if n <= 0:
			return 0
		elif n == 1:
			return 1
		else:
		 	return self.fibonacci(n-1) + self.fibonacci(n-2)
		
	def series(self):
		if self.terms <= 0:
			print("please enter a valid number")
			return
		print(f"Fibonacci series with {self.terms} terms: ")
		for i in range(self.terms):
			print(self.fibonacci(i), end=" ")
				 	
term = int(input("Enter the terms:"))
fib_seq = FibonacciGen(term)
fib_seq.series()
