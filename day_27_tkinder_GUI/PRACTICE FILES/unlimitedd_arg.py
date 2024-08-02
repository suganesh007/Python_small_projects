# todo: unlimited positional arguments
# the (*args)argument type is tuple and it is used to add unlimited arguments within the function
def add(*args):
    output = 0
    for i in args:
        output += i
    return output


addition = add(1, 2, 2, 5, 8, 6, 3, 6, 5, 8, 5, 6, 555)
print(addition)


# todo: it is a dict type
# TODO : the *args used to get more arguments and the **kwargs used to get more
#  arguments (args) with the keyword(kw) == kw + args = kwargs
def calci(n, **kwargs):
    # print(kwargs)
    output = n
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    output += kwargs["add"]
    output *= kwargs["mul"]
    return output


print(calci(2, add=2, mul=4))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        # self.model = kwargs["model"]

        # todo ::: it creates the error when there is no key is the dict so if we use get then
        #  the error does not occurs so get will be used but the work are same in both of the types


my_car = Car()
print(my_car.make)
