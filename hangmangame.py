#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:02:54 2021

@author: ksa
HangMan game code in python
"""
from random import randint as r

MAX_TRIES = 9
def loadwordlist(file):

    words = []
    with open(file) as listofwords:
        cpt= 0
        for word in listofwords:
            if len(word.strip()) < 5:
                continue
            words.append(word.strip())
            if cpt > 1000:
                break
            else:
                cpt += 1
    listofwords.close()
    return words

def display_word_guessed(word_guessed):
    print(''.join(word_guessed))

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch or ltr == ch.upper()]

# mylistofwords = loadwordlist('engmix2.txt')
mylistofwords = ['about', 'account', 'across', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 'almost', 'among', 'amount', 'amusement', 'angle', 'angry', 'animal', 'answer', 'apparatus', 'apple', 'approval', 'argument', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'automatic', 'awake', 'balance', 'basin', 'basket', 'beautiful', 'because', 'before', 'behaviour', 'belief', 'berry', 'between', 'birth', 'bitter', 'black', 'blade', 'blood', 'board', 'boiling', 'bottle', 'brain', 'brake', 'branch', 'brass', 'bread', 'breath', 'brick', 'bridge', 'bright', 'broken', 'brother', 'brown', 'brush', 'bucket', 'building', 'burst', 'business', 'butter', 'button', 'camera', 'canvas', 'carriage', 'cause', 'certain', 'chain', 'chalk', 'chance', 'change', 'cheap', 'cheese', 'chemical', 'chest', 'chief', 'church', 'circle', 'clean', 'clear', 'clock', 'cloth', 'cloud', 'collar', 'colour', 'comfort', 'committee', 'common', 'company', 'comparison', 'competition', 'complete', 'complex', 'condition', 'connection', 'conscious', 'control', 'copper', 'cotton', 'cough', 'country', 'cover', 'crack', 'credit', 'crime', 'cruel', 'crush', 'current', 'curtain', 'curve', 'cushion', 'damage', 'danger', 'daughter', 'death', 'decision', 'degree', 'delicate', 'dependent', 'design', 'desire', 'destruction', 'detail', 'development', 'different', 'digestion', 'direction', 'dirty', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 'distribution', 'division', 'doubt', 'drain', 'drawer', 'dress', 'drink', 'driving', 'early', 'earth', 'education', 'effect', 'elastic', 'electric', 'engine', 'enough', 'equal', 'error', 'event', 'every', 'example', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'false', 'family', 'father', 'feather', 'feeble', 'feeling', 'female', 'fertile', 'fiction', 'field', 'fight', 'finger', 'first', 'fixed', 'flame', 'flight', 'floor', 'flower', 'foolish', 'force', 'forward', 'frame', 'frequent', 'friend', 'front', 'fruit', 'future', 'garden', 'general', 'glass', 'glove', 'government', 'grain', 'grass', 'great', 'green', 'group', 'growth', 'guide', 'hammer', 'hanging', 'happy', 'harbour', 'harmony', 'healthy', 'hearing', 'heart', 'history', 'hollow', 'horse', 'hospital', 'house', 'humour', 'important', 'impulse', 'increase', 'industry', 'insect', 'instrument', 'insurance', 'interest', 'invention', 'island', 'jelly', 'jewel', 'journey', 'judge', 'kettle', 'knife', 'knowledge', 'language', 'laugh', 'learning', 'leather', 'letter', 'level', 'library', 'light', 'limit', 'linen', 'liquid', 'little', 'living', 'loose', 'machine', 'manager', 'market', 'married', 'match', 'material', 'measure', 'medical', 'meeting', 'memory', 'metal', 'middle', 'military', 'minute', 'mixed', 'money', 'monkey', 'month', 'morning', 'mother', 'motion', 'mountain', 'mouth', 'muscle', 'music', 'narrow', 'nation', 'natural', 'necessary', 'needle', 'nerve', 'night', 'noise', 'normal', 'north', 'number', 'observation', 'offer', 'office', 'operation', 'opinion', 'opposite', 'orange', 'order', 'organization', 'ornament', 'other', 'owner', 'paint', 'paper', 'parallel', 'parcel', 'paste', 'payment', 'peace', 'pencil', 'person', 'physical', 'picture', 'place', 'plane', 'plant', 'plate', 'please', 'pleasure', 'plough', 'pocket', 'point', 'poison', 'polish', 'political', 'porter', 'position', 'possible', 'potato', 'powder', 'power', 'present', 'price', 'print', 'prison', 'private', 'probable', 'process', 'produce', 'profit', 'property', 'prose', 'protest', 'public', 'punishment', 'purpose', 'quality', 'question', 'quick', 'quiet', 'quite', 'range', 'reaction', 'reading', 'ready', 'reason', 'receipt', 'record', 'regret', 'regular', 'relation', 'religion', 'representative', 'request', 'respect', 'responsible', 'reward', 'rhythm', 'right', 'river', 'rough', 'round', 'scale', 'school', 'science', 'scissors', 'screw', 'second', 'secret', 'secretary', 'selection', 'sense', 'separate', 'serious', 'servant', 'shade', 'shake', 'shame', 'sharp', 'sheep', 'shelf', 'shirt', 'shock', 'short', 'silver', 'simple', 'sister', 'skirt', 'sleep', 'slope', 'small', 'smash', 'smell', 'smile', 'smoke', 'smooth', 'snake', 'sneeze', 'society', 'solid', 'sound', 'south', 'space', 'spade', 'special', 'sponge', 'spoon', 'spring', 'square', 'stage', 'stamp', 'start', 'statement', 'station', 'steam', 'steel', 'stick', 'sticky', 'stiff', 'still', 'stitch', 'stocking', 'stomach', 'stone', 'store', 'story', 'straight', 'strange', 'street', 'stretch', 'strong', 'structure', 'substance', 'sudden', 'sugar', 'suggestion', 'summer', 'support', 'surprise', 'sweet', 'system', 'table', 'taste', 'teaching', 'tendency', 'theory', 'there', 'thick', 'thing', 'thought', 'thread', 'throat', 'through', 'through', 'thumb', 'thunder', 'ticket', 'tight', 'tired', 'together', 'tomorrow', 'tongue', 'tooth', 'touch', 'trade', 'train', 'transport', 'trick', 'trouble', 'trousers', 'twist', 'umbrella', 'under', 'value', 'verse', 'vessel', 'violent', 'voice', 'waiting', 'waste', 'watch', 'water', 'weather', 'weight', 'wheel', 'where', 'while', 'whistle', 'white', 'window', 'winter', 'woman', 'wound', 'writing', 'wrong', 'yellow', 'yesterday', 'young', 'Bernhard', 'Breytenbach', 'Android']


print(mylistofwords)
# print ("\033")
# print(chr(27) + "[2J")

playerpartymode = 0

while playerpartymode != 1 and playerpartymode != 2:
    playerpartymode = int(input('''Please selection your player mode:
    1 - One player Mode
    2- Two players mode : '''))

print(playerpartymode)
word_random_index = r(1,504)
word_to_guess = ""
if playerpartymode == 1:
    word_to_guess = input('''Player 1, Please enter the secret word the player 2 should guess : ''')
else:
    word_to_guess = mylistofwords[word_random_index]

if len(word_to_guess) > MAX_TRIES:
    MAX_TRIES = len(word_to_guess) + 5
length_of_the_word_guess = len(word_to_guess)


# print(length_of_the_word_guess)
# print("Word to guess : " + word_to_guess)
# print(find('Hi baby girl','h'))

found_secret_word = False

word_guessed = ['_'] * length_of_the_word_guess

number_of_tries = 0

while (not found_secret_word) and (number_of_tries < MAX_TRIES):
    number_of_tries += 1
    player_input = input(f'Please enter a word. This is the attempt number {number_of_tries}  out of {MAX_TRIES} allowed')
    list_of_occurrences = find(word_to_guess, player_input)
    print(list_of_occurrences)
    for index in list_of_occurrences:
        word_guessed[index] = player_input

    display_word_guessed(word_guessed)
    if len(find(word_guessed, '_')) == 0:
        found_secret_word = True

    print(chr(27) + "[2J")

if found_secret_word:
    print("Congratulation !!! You Won")
else:
    print(f'Oops !!! You lose the secret word was {word_to_guess}')

