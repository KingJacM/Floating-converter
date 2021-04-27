print("note: do not use this if binary form exceeds 9 places in total and if it starts in the second decimal place eg 0.011 in stead of 0.11")

whole_list = list(input("what is the binary form of your number?"))


if "." in whole_list:
	exponent = whole_list.index(".")
	whole_list.remove(".")
	if exponent == 1:
		whole_list.pop(0)
		exponent = 0
else:
	exponent = len(whole_list)

bin_of_exp = '{0:05b}'.format(exponent)

sign = input("Is this number negative? y/n")

sign_place = "0"

if sign == "y":
	sign_place = "1"
else:
	pass

string = "".join(whole_list)

fill_in = "0" * (9 - len(whole_list))

print(sign_place + string + fill_in + "0" + bin_of_exp)
