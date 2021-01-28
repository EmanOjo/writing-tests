
def is_positive(num):
    return True if num >= 0 else False
def is_even(num):
    return True if num % 2 == 0 else False
def describe_number(num):
    return {"is_positive":is_positive(num), "is_even":is_even(num)}
print(describe_number(2))
# only ever return once in a function- return stops your function