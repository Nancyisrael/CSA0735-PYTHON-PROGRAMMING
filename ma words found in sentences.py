def max_words_found(sentences):
   max_words=0
   for sentence in sentences:
       words=sentence.split()
       num_words=len(words)
       if num_words>max_words:
          max_words=num_words
   return max_words
sentences = ["alice and bob love apple", "i think so too", "this is great thanks very much"]
print("maximum words = ",max_words_found(sentences)) 
