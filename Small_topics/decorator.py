# A decorator is a function that takes another function and returns a modified version of it.

def add_sprinkles(func):
    def wrapper(*args,**kwrags):
        print("Sprinkles were added to ice-cream")
        func(*args,**kwrags)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwrags):
        print("Added fudge.")
        func(*args,**kwrags)
    return wrapper

    # add_fudge(get_icream) returns fudge_wrapper
    # add_sprinkles(fudge_wrapper) returns sprinkles_wrapper 
    # get_icream("chocolate") = sprinkles_wrapper("chocolate")

@add_sprinkles
@add_fudge
def get_icream(flavor):
    print(f"Here is your {flavor} ice-cream!")

get_icream("Chocolate")

# so get_icream function gets modififed by add_sprinkle and add_fudge function
# first add_sprinkles becomes get_icream = wrapper and add_fudge becomes get_icecream = wrapper 
# when ice cream is run giving argument the wrapper also get the argument