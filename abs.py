# Importing the necessary libraries for text processing
import nltk
nltk.download('punkt')
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Sample letter with improved cohesion and sentence structure
letter = """
Dear Sir/Madam,

I am writing to express my concern regarding the recent notification I received from your company regarding an impending increase in the insurance premium for my car, set to take effect next month.

As you may have noticed in your records, I have been a loyal customer of your company for nearly seven years. Throughout this period, I have maintained an impeccable driving record, never having been involved in any accidents or needing to file a claim.

While I understand that periodic adjustments to pricing may be necessary, I was surprised to learn that the proposed increase would result in a substantial 20% rise in my monthly premium. This significant increase has prompted me to seek clarification regarding the rationale behind this decision.

I kindly request that you provide a detailed explanation for the substantial premium hike. Understanding the factors contributing to this increase will help me make an informed decision about whether to continue my insurance coverage with your company. 

Should you be unable to provide a satisfactory justification for the proposed rate hike, I may regrettably have no choice but to explore alternative insurance options with other providers.

I eagerly anticipate your response and hope that you can shed light on the reasons for this substantial premium increase. 

Yours faithfully,
Jay
"""

# Tokenizing the letter into sentences
sentences = sent_tokenize(letter)

# Tokenizing the letter into words and removing stopwords for cohesion analysis
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(letter)
filtered_word_tokens = [word for word in word_tokens if word.lower() not in stop_words]

# Printing the improved letter
print("\n".join(sentences))
