import pickle
txt_file = open("code1.txt", "rb")
bin_file = open("code2.txt", "wb")
txt_code = pickle.load(txt_file)
print(txt_code)
pickle.dump(txt_code, bin_file)
txt_file.close()
bin_file.close()
earth_weight = input("Your weight on Earth: ")
moon_weight = earth_weight * 0.165
weight_gained_each_year = input("Let's say you gain the same amount of weight each year. If you gained ")
number_of_years = input("pounds on Earth every year and weighed yourself on the moon every year for ")
print "years, each year on the moon you would weigh this much:"
year_number = 1
for years in range(0, number_of_years):
	moon_weight = earth_weight * 0.165
	print "Year %s: %s pounds on the moon, %s pounds on Earth" %(str(year_number), str(moon_weight), str(earth_weight))
	earth_weight += weight_gained_each_year
	year_number += 1