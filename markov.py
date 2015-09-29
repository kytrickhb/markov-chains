from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = open(file_path).read()
    return text


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    word_list = []
    # construct a list out of the text_string
    for word in text_string.strip().split():
         word_list.append(word)
    
    # construct a dictionary where keys are bi-grams and values are a list of the tri-words
    for i in range(len(word_list)-2):
        if (word_list[i], word_list[i+1]) not in chains:
            chains[(word_list[i], word_list[i+1])] = [word_list[i+2]]
        else:
            chains[(word_list[i], word_list[i+1])].append(word_list[i+2])

    #print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    digram = choice(chains.keys()) #this selects a random key (tuple) from chains (starting point)
    text = text + " " + digram[0] + " " + digram[1]
    while True:
        try:
            digram = digram[1], choice(chains[digram])
            text = text + " " + digram[1]
        except KeyError:
            break
        print digram

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text