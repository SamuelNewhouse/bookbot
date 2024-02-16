book_file = "books/frankenstein.txt"

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
	with open(book_file) as f:
		file_contents = f.read()

	word_count = count_words(file_contents)
	letter_counts = count_letters(file_contents)
	letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
	letter_counts = filter(lambda x: x[0].isalpha(), letter_counts)

	print(f"--- Begin report of {book_file} ---")
	print(f"{word_count} words found in the document")
	for count in letter_counts:
		print(f"The '{count[0]}' character was found {count[1]} times")

main()