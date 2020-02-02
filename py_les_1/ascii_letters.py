component_list = [
    '     ', #0
    '#   #', #1
    '  #  ', #2
    ' ### ', #3
    ' # # ', #4
    ' #   ', #5
    '#    ', #6
    ' ##  ', #7
    '  ## ', #8
    '# # #', #9
    '## ##', #10
    '##  #', #11
    '#  ##', #12
    '   # ', #13
]

alphabet = {
    'A': [2, 4, 3, 4, 1],
    'B': [3, 4, 3, 4, 3],
    'C': [3, 5, 5, 5, 3],
    'D': [7, 4, 4, 4, 7],
    'E': [3, 5, 7, 5, 3],
    'F': [3, 5, 3, 5, 5],
    'G': [8, 5, 3, 4, 2],
    'H': [4, 4, 3, 4, 4],
    'I': [2, 0, 2, 2, 2],
    'J': [2, 0, 2, 2, 5],
    'K': [4, 7, 5, 4, 7],
    'L': [5, 5, 5, 5, 3],
    'M': [1, 10, 9, 1, 1],
    'N': [1, 11, 9, 12, 1],
    'O': [3, 4, 4, 4, 3],
    'P': [3, 4, 3, 5, 5],
    'Q': [3, 4, 4, 3, 13],
    'R': [3, 4, 3, 5, 4],
    'S': [8, 5, 2, 13, 7],
    'T': [3, 2, 2, 2, 2],
    'U': [4, 4, 4, 4, 2],
    'V': [1, 1, 4, 4, 2],
    'W': [1, 1, 9, 4, 4],
    'X': [1, 4, 2, 4, 1],
    'Y': [1, 4, 2, 2, 2],
    'Z': [3, 13, 2, 5, 3],
    ' ': [0, 0, 0, 0, 0]
}


def get_transcription(sentence):
    sentence = sentence.upper()
    result_art = ''
    for line in range(0, 5):
        for char in sentence:
            if not alphabet.__contains__(char):
                print('Error: illegal symbol')
                return ''
            result_art += component_list[alphabet.get(char)[line]]
        result_art += '\n'
    return result_art


user_input = input("Enter the smth: ")
print(get_transcription(user_input))
