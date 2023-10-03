# problem 1
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return zip_code == 5 and zip_code.isdigit()

# problems 2 & 3
doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    indices = []
    for i in range(len(doc_list)):
        list = doc_list[i]
        if keyword.lower() in list.lower():
            indices.append(i)
    return indices
print(word_search(doc_list, 'casino'))


def multi_word_search(documents, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """

    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices

print(multi_word_search(doc_list, ['casino', 'they']))