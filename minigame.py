from wonderwords import *
from TranslationProgram import *

class RandomGenerator():
    def __init__(self, category, d, f):
        self.category = category
        self.d = d
        self.f = f

    def generate(self):
        if self.category == 0:
            w = RandomWord()
            ww = w.word()
            wt = ww
            tw = translate(wt, self.d, self.f)
            return ww, tw
        else:
            s = RandomSentence()
            ss = s.simple_sentence()
            st = ss
            ts = translate(st, self.d, self.f)
            return ss, ts

def guessgame(n):
    if n == 0:
        word_gen = RandomGenerator(0, 1, 3)#0 = generate word; 0/1 = translate words in sentence/whole sentence; frequency of translation from 1-n
        word_pair = word_gen.generate()
        print("Word to translate:", word_pair[0])
        print("Translated word:", word_pair[1])
        guess_word = input("Enter your guess for the translated word: ")
        if guess_word == word_pair[0]:
            print("Correct!")
        else:
            print("Incorrect.")
    else:
        sent_gen = RandomGenerator(1, 1, 10)#1 = generate sentence; 0/1 = translate words in sentence/whole sentence; frequency of translation from 1-n
        sent_pair = sent_gen.generate()
        print("\nSentence to translate:", sent_pair[0])
        print("Translated sentence:", sent_pair[1])
        guess_sent = input("Enter your guess for the translated sentence: ")
        if guess_sent == sent_pair[0]:
            print("Correct!")
        else:
            print("Incorrect.")


#guessgame(0)#play either word or sentence