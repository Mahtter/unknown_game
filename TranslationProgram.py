import random
import re
from deep_translator import GoogleTranslator

def translate_text(text, frequency, d):
    if d == 0:
        return translate_sentences(text, frequency)
    else:
        return translate_words(text,frequency)

def translate_sentences(text, frequency):
    sentence_pattern = re.compile(r'(?<=[.!?])\s+')
    sentences = sentence_pattern.split(text)
    translated_sentences = []
    for i in range(0, len(sentences), frequency):
        sentence = sentences[i]
        try:
            translated_sentence = GoogleTranslator(source='auto', target='es').translate(sentence)
            translated_sentences.append(translated_sentence)
        except Exception as e:
            print(f"Error translating sentence '{sentence}': {e}")
    
    return '. '.join(translated_sentences)

def translate_words(sentence, frequency):
    words = sentence.split()
    translated_words = []
    for i, word in enumerate(words):
        if i % frequency == 0:
            try:
                translated_word = GoogleTranslator(source='auto', target='es').translate(word)
                translated_words.append(translated_word)
            except Exception as e:
                print(f"Error translating word '{word}': {e}")
        else:
            translated_words.append(word)
    
    return ' '.join(translated_words)

def adjust_punctuation(original_text, translated_text):
    # Remove duplicated punctuation marks in translated_text
    translated_text = re.sub(r'([.!?])\1+', r'\1', translated_text)
    
    # Replace any '.' with '.' in original_text
    adjusted_translated_text = translated_text.replace('.', '.')
    # Replace any '?' with '?' in original_text
    adjusted_translated_text = adjusted_translated_text.replace('?', '?')
    # Replace any '!' with '!' in original_text
    adjusted_translated_text = adjusted_translated_text.replace('!', '!')
    
    return adjusted_translated_text

def translate(long_text, d,f):
    frequency = random.randint(1, f)  # Randomly select the frequency of translation

    new_text = translate_text(long_text, frequency, d)
    adjusted_text = adjust_punctuation(long_text, new_text)
    return adjusted_text



