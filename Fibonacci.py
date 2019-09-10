#Write a function that gives the Nth number of the Fibonacci Sequence

def Fibonacci (Number):

	if Number == 0: 
		print (0)
		return
	elif Number == 1: 
		print (1)
		return
	else:
		index = 2
		second_back = 0
		first_back = 1
		while index <= Number: 
			Fib_number = first_back + second_back 
			second_back = first_back
			first_back = Fib_number
			index += 1	
		print (Fib_number)
Fibonacci (2)
