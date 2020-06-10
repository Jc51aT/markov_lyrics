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
    model = gen_model(lyrics, order)
    curr_frag = lyrics[random.randint(0,len(lyrics)-1)]
    output= ""
    for j in range(length-order):
        new_word = get_next_word(model, curr_frag)
        output += new_word + " "
        curr_frag = new_word
    print(output)



text = """See, my pedigree most definitely don't tolerate the front
Shit I've been through prolly offend you
This is Paula's oldest son
I know murder, conviction
Burners, boosters, burglars, ballers, dead, redemption
Scholars, fathers dead with kids
And I wish I was fed forgiveness
Yeah, yeah, yeah, yeah, soldier's DNA
Born inside the beast
My expertise checked out in second grade
When I was nine, on cell, motel, we didn't have nowhere to stay
At twenty-nine, I've done so well, hit cartwheel in my estate
And I'm gon' shine like I'm supposed to antisocial, extrovert
And excellent mean the extra work
And absent-ness what the fuck you heard
And pessimists never struck my nerve
And that's a riff, gonna plead this case
The reason my power's here on earth
Salute the truth, when the prophet say"""
text = text.translate(str.maketrans('', '', string.punctuation))
text = text.split()

if __name__ == "__main__":
    generate_lyrics(text, int(sys.argv[1]), int(sys.argv[2]))