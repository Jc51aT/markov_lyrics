import numpy as np
import random
import sys
import string 

def gen_model(text, order=2):
    model = {}
    
    for i in range(0, len(text)- order):
        fragment = text[i] 
        next_word = text[i+1]
        if fragment not in model:
            model[fragment] = {}
        if next_word not in model[fragment]:
            model[fragment][next_word] = 1
        else:
            model[fragment][next_word] += 1
    return model

def get_next_word(model, fragment):
    wr = []
    for w in model[fragment]:
        for i in range(0, model[fragment][w]):
            wr.append(w)
    return random.choice(wr)

def generate_lyrics(lyrics, order=2, length=100):
    text = lyrics
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split()
    lyrics = text
    model = gen_model(lyrics, order)
    curr_frag = lyrics[random.randint(0,len(lyrics)-1)]
    output= ""
    for j in range(length-order):
        new_word = get_next_word(model, curr_frag)
        output += new_word + " "
        curr_frag = new_word
    return output


if __name__ == "__main__":
    generate_lyrics(text, int(sys.argv[1]), int(sys.argv[2]))