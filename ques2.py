import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer

# Download necessary NLTK data
nltk.download('wordnet')
nltk.download('omw-1.4')

# Tokenized words after stopword removal (from Q1)
filtered_words = ['fascinated', 'world', 'technology', 'every', 'day', 'new', 
                  'innovations', 'like', 'artificial', 'intelligence', 'robotics', 
                  'quantum', 'computing', 'reshaping', 'lives', 'technology', 
                  'makes', 'communication', 'faster', 'knowledge', 'accessible', 
                  'businesses', 'efficient', 'love', 'learning', 'cuttingedge', 
                  'gadgets', 'smart', 'home', 'devices', 'software', 'simplify', 
                  'daily', 'tasks', 'future', 'technology', 'excites', 'holds', 
                  'endless', 'possibilities', 'creativity', 'problemsolving']

# 2. Apply Stemming
porter = PorterStemmer()
lancaster = LancasterStemmer()

porter_stemmed = [porter.stem(word) for word in filtered_words]
lancaster_stemmed = [lancaster.stem(word) for word in filtered_words]

# 3. Apply Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered_words]

# 4. Compare and Display Results
print("Original Words:\n", filtered_words)
print("\nPorter Stemmer Results:\n", porter_stemmed)
print("\nLancaster Stemmer Results:\n", lancaster_stemmed)
print("\nWordNet Lemmatizer Results:\n", lemmatized)
