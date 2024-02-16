book_file = "books/frankenstein.txt"

def count_letters(text):
	letter_counts = {}

	for c in [x for x in text.lower() if x.isalpha()]:
		if c in letter_counts:
			letter_counts[c] += 1
		else:
			letter_counts[c] = 1

	return letter_counts

def count_words(text):
	return len(text.split())

def main():
	with open(book_file) as f:
		file_contents = f.read()

	word_count = count_words(file_contents)
	letter_counts = count_letters(file_contents)
	letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

	print(f"--- Begin report of {book_file} ---")
	print(f"{word_count} words found in the document\n")

	for char, count in letter_counts:
		print(f"The '{char}' character was found {count} times")

	print("--- End report ---")

main()