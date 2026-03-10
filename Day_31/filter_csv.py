import pandas as pd

# data = pd.read_csv("b1-goethe-liste-with-english.csv")
# word_dict = {
#     "German": [],
#     "English": []
# }

# for num, ger in enumerate(data['word']):
#     german_word = ger.split(",")[0]
#     english_word = data['english_meaning'][num]
#     word_dict['German'].append(german_word)
#     word_dict['English'].append(english_word)

# filter_dict = pd.DataFrame(word_dict)
# filter_dict.to_csv("b1_vocab.csv", index=False)

data = pd.read_csv("b1_vocab.csv")
word = data.to_dict(orient="records")
print(word)
