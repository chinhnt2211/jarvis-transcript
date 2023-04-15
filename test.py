import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, words, wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('stopwords')


stop_words = set(stopwords.words('english'))
english_words = set(words.words())
lemmatizer = WordNetLemmatizer()



text = "I was born and raised in the heart of Hanoi city it's balls. I love Hanoi and my life right now. My family lives in an apartment in Dong Da district. The cost to live here is quite high. My parents have to work a lot to make sure I live the most comfortable. Everyone here is very sociable and friendly. Because it is the city center, it is always crowded and bustling here. You can buy anything you want. There are many shops selling different items to choose from. You can go anywhere with the bus. When you live in the city, you will be very familiar with the malls. This is a place for shopping and also a place for entertainment. My parents will take me to the mall once a week to buy essential items for my family and myself. I joined a badminton club in the apartment complex to exercise after stressful school hours. One feature of the city that I like very much is that its roads are very flat and easy to navigate. Night food in Hanoi is a culmination. You can easily find a great place to eat here. Life in the city has many wonderful things. That is the reason so many people have always wanted to be able to live here. I always try to deserve the wonderful life my parents give me."


tokens = word_tokenize(text)

filtered_tokens = [word for word in tokens if word.lower() in english_words]
filtered_tokens = [word for word in filtered_tokens if word.lower() not in stop_words]
filtered_tokens = [lemmatizer.lemmatize(
    word.lower(), "v") for word in filtered_tokens if word.isalnum()]
filtered_tokens = [lemmatizer.lemmatize(
    word.lower(), "n") for word in filtered_tokens if word.isalnum()]

print(filtered_tokens)