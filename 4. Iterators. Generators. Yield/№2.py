# 				2. Генератор, который принимает список списков, и возвращает их плоское представление
number_one = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(lists):
	for liste in lists:
		for list in liste:
			yield list

if __name__ == "__main__":
	for item in flat_generator(number_one):
		print(item)