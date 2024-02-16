def count_letters(str):
	letter_counts = {}

	for c in str.lower():
		if c in letter_counts:
			letter_counts[c] += 1
		else:
			letter_counts[c] = 1

	return letter_counts

def count_words(str):
	return len(str.split())

def main():
	with open("books/frankenstein.txt") as f:
		file_content = f.read()

	print(f"Book contains {count_words(file_content)} words.")
	print(f"Letter counts: \n")
	print(count_letters(file_content))

main()