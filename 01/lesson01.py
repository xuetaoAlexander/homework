#!/usr/bin/env python
# coding=utf-8

import jieba
import random
from collections import Counter

def generate(grammar_rule, target):
    if target in grammar_rule: # names 
        candidates = grammar_rule[target]  # ['name names', 'name']
        candidate = random.choice(candidates) #'name names', 'name'
        return ''.join(generate(grammar_rule, target=c.strip()) for c in candidate.split())
    else:
        return target

def get_generation_by_gram(grammar_str: str, target, stmt_split='=>', or_split='|'):

    rules = dict() 
    for line in grammar_str.split('\n'):
        if not line: continue
        # skip the empty line
      #  print(line)
        stmt, expr = line.split(stmt_split)
    
        rules[stmt.strip()] = expr.split(or_split)
    
    generated = generate(rules, target=target)
    
    return generated


with open('/home/xuetaozhang/kaikeba/homework/01/pre_movie_comments.csv') as pre_movie:
    movie = pre_movie.read()

with open('/home/xuetaozhang/kaikeba/homework/01/pre_train.txt') as pre_train:
    train = pre_train.read()

corpus = movie + train

print(len(movie))
print(len(train))
print(len(corpus))

def cut(string):
    return list(jieba.cut(string))

TOKENS = cut(corpus)
words_count = Counter(TOKENS)

_2_gram_words = [
    TOKENS[i] + TOKENS[i+1] for i in range(len(TOKENS)-1)
]

_2_gram_word_counts = Counter(_2_gram_words)

def get_gram_count(word, wc):
    if word in wc: return wc[word]
    else:
        return wc.most_common()[-1][-1]

def two_gram_model(sentence):
    # 2-gram langauge model
    tokens = cut(sentence)
    
    probability = 1
    
    for i in range(len(tokens)-1):
        word = tokens[i]
        next_word = tokens[i+1]
        
        _two_gram_c = get_gram_count(word+next_word, _2_gram_word_counts)
        _one_gram_c = get_gram_count(next_word, words_count)
        pro =  _two_gram_c / _one_gram_c
        
        probability *= pro
    
    return probability


print(two_gram_model('此外自本周6月12日起除小米手机6等15款机型'))
print(two_gram_model('前天早上吃晚饭的时候'))
print(two_gram_model('前天早上吃早饭的时候'))
print(two_gram_model('我请你吃火锅'))
print(two_gram_model('这个人来自清华大学'))
print(two_gram_model('这个人来自秦华大学'))



all_corpus = []
def generate_best(grammar_str, target, n):
    for i in range(n):
        gen_sentence = get_generation_by_gram(grammar_str, target)
        prob = two_gram_model(gen_sentence)
        all_corpus.append((gen_sentence, prob))
    all_corpus_sorted = sorted(all_corpus, key = lambda x : x[1], reverse = True)
    return all_corpus_sorted[0][0]

simple_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => Adj | Adj Adj*
verb_phrase => verb noun_phrase
Article =>  一个 | 这个
noun =>   女人 |  篮球 | 桌子 | 小猫
verb => 看着   |  坐在 |  听着 | 看见
Adj =>   蓝色的 |  好看的 | 小小的"""

best_sentence = generate_best(simple_grammar, 'sentence', 100)
print(best_sentence)



