import phonenumbers

my_string_number = "+91990233433"
my_number = phonenumbers.parse(my_string_number)

print(phonenumbers.is_possible_number(my_number))