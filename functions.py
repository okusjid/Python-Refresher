def my_func():
    print("My first python function")


my_func()


def my_fun_with_params(a='hello'):
    print("{}, We are using parms.".format(a))


my_fun_with_params()
my_fun_with_params("Namaste")

def fun_with_return(a,b):
    if(type(a) and type(b)) == type(1):
        return a+b
    else:
        return ("Sorry, We need Integers")

Sum = fun_with_return(5,2)
print(Sum)

Sum2 = fun_with_return("abc","abc")
print(Sum2)

# Lambda Expressions

# Filter --> Without Lambda
mylist = [1,2,3,4,5,6,7]

def even_bool(num):
    return num%2 == 0

even = filter(even_bool,mylist)
print(list(even))

# Filter With Lambda
new_list = range(30)
even_with_lambda =filter(lambda num:num%2 == 0, new_list)
print(list(even_with_lambda))
