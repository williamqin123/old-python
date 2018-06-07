import types
indent_number = 1
tab_size = ""
count = 0
def create_list(list, indent = 4):
	global indent_number, tab_size, count
	indent_size = " " * indent
	list_all = list
	for item in list_all:
		if type(item) == types.ListType:
			count = 0
			for nested_item in list_all:
				count += 1
			tab_size = indent_size * indent_number
			indent_number += 1
			create_list(list = item, indent = indent)
			print "%s________________" % tab_size
		else:
			if count == indent_number:
				list_all = list
				tab_size = indent_size * (indent_number - 1)
				indent_number -= 1
			print tab_size + str(item), [count, indent_number]
create_list(list = [0, [1, [2, 2, 2], 1], 0, [1, 1], 0])