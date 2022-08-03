entered_word = input('Enter word: ')
def palindrome():
    result_word = (entered_word[::-1])
    print(entered_word == result_word)


palindrome()

# second case

def palindrome():
    entered_word_list = list(entered_word)
    entered_word_list.reverse()
    result_word = ''
    result_word = result_word.join(entered_word_list)
    print(result_word == entered_word)


palindrome()
