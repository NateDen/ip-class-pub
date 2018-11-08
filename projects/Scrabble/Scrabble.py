from flask import *
import math
import itertools
import os
import string

app = Flask(__name__, template_folder = 'Templates')


def find_words(letters, language_dictionary): #letters will be a list
    preliminary_list_of_words = []
    list_of_words = []
    if '*' in letters:
        alphabet = list(string.ascii_lowercase)        
        wildcard_index = letters.index('*')
        del(letters[wildcard_index])        
        
        for item in alphabet:
            letters.append(item)
            for i in range(len(letters)):
                letters_to_words = list(itertools.permutations(letters, i + 1))
                for item in letters_to_words:
                    preliminary_list_of_words.append(''.join(item))
            wildcard_status = ['item']
            
            del(letters[-1])  
          
    else:
        for i in range(len(letters)):
            letters_to_words = list(itertools.permutations(letters, i + 1))
            for item in letters_to_words:
                preliminary_list_of_words.append(''.join(item))             
 
    american_dictionary_path = os.path.abspath('/usr/share/dict/american-english')
    british_dictionary_path = os.path.abspath('/usr/share/dict/british-english')   
    
    if language_dictionary == 'american_dictionary':
        american_dictionary = open(american_dictionary_path, 'r')
        american_words = set()
        for item in american_dictionary:
            item = item.rstrip('\n')
            american_words.add(item)
            
        for potential_word in preliminary_list_of_words:
            if potential_word in american_words:
                list_of_words.append(potential_word)
    else:
        british_dictionary = open(british_dictionary_path, 'r')
        british_words = set()
        for item in british_dictionary:
            item = item.rstrip('\n')
            british_words.add(item)    
            
        for potential_word in preliminary_list_of_words:
            if potential_word in british_words:
                list_of_words.append(potential_word)                
                
    return list_of_words

def find_word_values(words):
    letter_score = dict.fromkeys(['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't'], 1)
    letter_score.update(dict.fromkeys(['d', 'g'], 2))
    letter_score.update(dict.fromkeys(['b', 'c', 'm', 'p'], 3))
    letter_score.update(dict.fromkeys(['f', 'h', 'v', 'w'], 4))
    letter_score.update(dict.fromkeys(['k'], 5))
    letter_score.update(dict.fromkeys(['j', 'x'], 8))
    letter_score.update(dict.fromkeys(['q', 'z'], 10)) 
    letter_score.update(dict.fromkeys(['*'], 0))    
    word_and_length_and_score = set()
    list_of_letters = []
    
    for i in range(7):
        form_item_name = ('letter' + str(i + 1))
        if request.form[form_item_name] != '':            
            list_of_letters.append(request.form[form_item_name])   
            
    for word in words: 
        word_score = 0
        word_length = len(word)
        for letter in word:            
            if letter not in list_of_letters or list_of_letters.count(letter) < word.count(letter):
                word_score += 0
            else:
                word_score += letter_score[letter]
            
        word_and_length_and_score.add((word, word_length, word_score))
        
    return word_and_length_and_score
 
@app.route('/results',methods = ['POST', 'GET'])
def results():
    if request.method == 'POST':
        #need to get which dictionary that user selected as well
        list_of_letters = []
        existing_letters = ''       
        if request.form.getlist('attach') and request.form['existing_letters'] != '':           
            existing_letters += request.form['existing_letters']

        for i in range(7):
            form_item_name = ('letter' + str(i + 1))
            if request.form[form_item_name] != '':
                
                list_of_letters.append(request.form[form_item_name])  
                if existing_letters != '':
                    list_of_letters.append(existing_letters)  
                    
                get_words = find_words(list_of_letters, request.form['language_dictionary'])
                get_word_values = find_word_values(get_words)

        return render_template("results.html", word_and_length_and_score = get_word_values)

@app.route('/')
def hello_world():    
    return render_template('base.html')

if __name__ == '__main__':
    app.debug = True
    debug = True
    app.run(debug = True)