my_dict = {"Михаил" : 1972, "Соня" : 1981}
print(my_dict)
print(my_dict["Михаил"])
my_dict["Стас"] = 2003
print(my_dict)
my_dict.update({"Никита" : 2017, "Татьяна" : 1948})
print(my_dict)
print(my_dict.get("Агнессэ"))
a = my_dict.pop("Татьяна")
print(a)
print(my_dict)