import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import string

# Downloading necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Original paragraph
text = """I’m fascinated by the world of technology. Every day, new innovations like artificial intelligence, robotics, and quantum computing are reshaping our lives. Technology makes communication faster, knowledge more accessible, and businesses more efficient. I love learning about cutting-edge gadgets, smart home devices, and software that simplify daily tasks. The future of technology excites me because it holds endless possibilities for creativity and problem-solving."""

# 1. Convert text to lowercase and remove punctuation
text_lower = text.lower()
text_clean = text_lower.translate(str.maketrans('', '', string.punctuation))

# 2. Tokenize the text into words and sentences
word_tokens = word_tokenize(text_clean)
sentence_tokens = sent_tokenize(text_clean)

# 3. Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in word_tokens if word not in stop_words]

# 4. Display word frequency distribution (excluding stopwords)
freq_dist = FreqDist(filtered_words)

print("Word Tokens:\n", word_tokens)
print("\nSentence Tokens:\n", sentence_tokens)
print("\nFiltered Words (No Stopwords):\n", filtered_words)
print("\nWord Frequency Distribution:\n")
freq_dist.plot()

