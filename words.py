def print_upper_words(words):
    """Given list of words, print out the words in uppercaes

    For example:
    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

    Should print:
    HELLO
    HEY
    GOODBYE
    YO
    YES
    """
    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words_e(words):
    """Given list of words, print out words, starting with e, in uppercase

    For example:
    print_upper_words_e(["even", "test", "eleven", "elf", "elmo"])

    Should print:
    EVEN
    ELEVEN
    ELF
    ELMO
    """
    for word in words:
        if word.startswith('e'):
            print(word.upper())

print_upper_words_e(["even", "test", "eleven", "elf", "elmo"])

def print_upper_words_with(words, must_start_with):
    """Given list of words, print out the words in uppercase, specifying what letters
    to start with the object 'must_start_with'

    For example:
    print_upper_words_with(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
    Should print:
    HELLO
    HEY
    YO
    YES
    """
    for word in words:
        if word[0] in must_start_with:
            print(word.upper())

print_upper_words_with(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})