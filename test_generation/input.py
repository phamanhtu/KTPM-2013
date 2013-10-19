# Phạm Anh Tú/ K55CLC
import math
def is_triangle(a , b , c):
	if a<b+c and b<a+c and c<a+b:
		return True
	return False
	pass

def is_equilateral(a , b , c):
	if a==b==c:
		return True
	return False
	pass

def is_isosceles(a , b , c):
	if a==b or b==c or c==a:
		return True
	return False
	pass

def main(a , b ,c):
	'''
	a:[0;13][14;21]
	b:[0;10][11;20]
	c:[0;10]
	'''
	if is_triangle(a , b , c):
		if is_equilateral(a , b ,c):
			return 'is_equilateral'
		elif is_isosceles(a , b ,c):
			return "is_isosceles"
		else:
			return "is_triangle"
	else:
		return "not is triangle"
# if __name__ == "__main__":

# 	import doctest
# 	doctest.testmod()