import re
from collections import Counter
text = "This is is a sample text. This text contains some some sample words. Sample words are repeated in this text."
words = re.findall(r'\b\w+\b', text.lower())
word_count = Counter(words)
repeated_words = [word for word, count in word_count.items() if count > 1]
print(repeated_words)