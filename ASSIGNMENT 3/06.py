from sys import getsizeof

text = input("ENTER THE TEXT : ")
print(f"THE TYPE OF THE TEXT  {text} : {type(text)}")
print(f"THE MEMORY ADDRESS OF THE TEXT  {text} : {id(text)}")
print(f"SIZE IN BYTES OF THE VARIABLE {text} : {getsizeof(text)}")

'''
OUTPUT : ENTER THE TEXT : 10
THE TYPE OF THE TEXT  10 : <class 'str'>
THE MEMORY ADDRESS OF THE TEXT  10 : 1665740136848
SIZE IN BYTES OF THE VARIABLE 10 : 43

'''
