import re

def most_common_word(paragraph, banned):
    banned_set = {x.lower() for x in banned}
    paragraph = paragraph.lower()
    paragraph = re.sub(r"[!?',;.]", ' ', paragraph)
    
    words = paragraph.split()
    
    word_frequency = {}
    max_count = 0
    most_freq_word = ''
    
    for word in words:
        if word not in banned_set:
            word_frequency[word] = word_frequency.get(word, 0) + 1
            
            if word_frequency[word] > max_count:
                max_count = word_frequency[word]
                most_freq_word = word
            
    return most_freq_word
    