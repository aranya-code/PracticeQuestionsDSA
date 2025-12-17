"""

Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

count_word_frequency(words) 

Output:

 {'apple': 3, 'orange': 2, 'banana': 1}
 
 """

def count_word_frequency(words):
    frequency ={}
    for word in words:
        
        if word in frequency:
            frequency[word] +=1
        else:
            frequency[word]=1
    return frequency

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))