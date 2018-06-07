class Translator:
	def create_code(self):
		self.code_dict = input()
	def translate(self, code):
		split_code = code.split()
		for number in split_code:
			if not number == " ":
				number = self.code_dict[number]
		print(split_code)
translator = Translator()
translator.create_code()
while True:
	code = raw_input("Secret Code: ")
	translator.translate(code)