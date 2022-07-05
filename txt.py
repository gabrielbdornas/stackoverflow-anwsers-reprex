def input_text():
	f = open('text.txt', 'a')
	txt = input('text : ')
	f.write(f'{txt}\n')
	f.close