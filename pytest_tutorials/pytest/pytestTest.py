import pytest

def func(x):
	return x+1

def test():
	assert func(3) == 4

def main():
	test()




if __name__ == "__main__":
	print("hi")	##main()
	main()
