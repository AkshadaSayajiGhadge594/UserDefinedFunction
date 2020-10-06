##############################################################
# Consider below Application which demonstrate different concepts that we can apply while defining user defined functions
###############################################################

print("---------------JAY SADGURU-------------");
print("--------Akshada Sayaji Ghadge--------");
print("-----Demonstrate of advanced Functions-------");

# Function which accepts nothing and return nothing

def Marvellous1():
	print("Inside Marvellous1");

# Function which accept value and return nothing

def Marvellous2(value):
	print("Inside Marvellous2");
	print("Accepted value is",value);

# function which accepts value and return value 

def Marvellous3(value):
	print("Inside Marvellous3");
	print("Accepted value is",value);
	return value+1;

# Function Which accepts multiple values and return multiple value

def Marvellous4(value1,value2):
	print("Inside MArvellous4");
	add = value1+value2;
	sub = value1-value2;
	return add,sub;
# Function which call another function which is defined outside it

def Marvellous5():
	print("Inside Marvellous5");
	Marvellous1();

# function which contain another nested function defined in it

def Marvellous6():
	print("Inside Marvellous6");
	def InnerFun():
		print("Inside InnerFun");
	InnerFun();   # ethun line no 44 la janar (function call)

# Functions calls for above functions

no = 11;

Marvellous1();
Marvellous2(no);
ret = Marvellous3(no);
print("Return value is",ret);

Marvellous5();

ret1,ret2 = Marvellous4(10,4);
print("Addition is ",ret1);
print("Substraction is",ret2);

Marvellous6();


