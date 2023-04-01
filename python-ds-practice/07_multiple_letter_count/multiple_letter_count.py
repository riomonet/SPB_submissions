def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    p = set(phrase)
    dict = {}
    for letter in p :
        count = phrase.count(letter)
        dict[letter] = count
    return dict
    


