# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:47:49 2019

@author: HP
"""
import Avicii
#creating a dictionary from a lyric
lyrics = Avicii.lyrics

def lyrics_to_frequencies(lyrics):
    """
    lyrics: a list of words in a lyric
    return: returns a dictionary with words as key 
    and number of times they appear as value
    
    """
    word_dict = {}
    for word in lyrics:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

#most common words in a lyric

def most_common_words(freq_dict):
    """
    freq_dict: a dictionary with words as key and
    number of times they appear on a lyric as int
    returns a list of words or word that appear the most
    and the number of times it appears
    """
    frequency = freq_dict.values()
    most_freq = max(frequency)
    
    words_list = []
    for f in freq_dict:
        if freq_dict[f] == most_freq:
            words_list.append(f)
    return (words_list, most_freq)

def words_often(freq_dict, minTimes):
    """
    freq_dict: a dictionary with words as key and
    number of times they appear on a lyric as int
    minTimes : minimum number of times
    return : list of words and frequencies above or equal
    to minTimes
    """
    result = []
    done = False
    while not done:
        temp = most_common_words(freq_dict)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freq_dict[w])
        else:
            done = True
    return result
                





