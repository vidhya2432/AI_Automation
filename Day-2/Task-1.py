##Text Analyzer

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

total_words = len(words)
unique_words = set(words)
python_count = words.count("python")

print("Total words:", total_words)
print("Unique words:", len(unique_words))
print("Python count:", python_count)