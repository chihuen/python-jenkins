def add(a, b):
	if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
   		raise TypeError("a and b should be number")
	return a + b
  

