import sys

def hail_friend(names):
    names_str = ", ".join(names)
    print(f"Hail, {names_str}!")

hail_friend(sys.argv[1:])

#New Addition Return Values
def add_numbers(first_number, second_number):
    result_sum = first_number + second_number
    return result_sum
print(add_numbers(1, 2))