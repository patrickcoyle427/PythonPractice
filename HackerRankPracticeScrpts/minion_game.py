#!usr/bin/python3

'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, s.
Both players have to make substrings using the letters of the string s.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string s.

For Example:
String = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
'''


def minion_game(word):

    vowels = 'AEIOU'
    stuart = 0
    # stuart cares about words that start with consenants
    kevin = 0
    # kevin cares about words that start with vowels

    for i in range(len(word)):

        if word[i] in vowels:
        
        # checks if the letter currently being checked is in vowels

            kevin += (len(word) - i)
            # How this works: if the string starts with the found letter,
            # there is one substring for each letter (the length) of that string,

            # in BANANA:
            # a is found first, so now we know that the following substrings can
            # be found in this string:
            # a, an, ana, anan, anana, which is 5.
            # the length of that substring (ANANA), is equal to the number
            # of substrings found, SO by taking the length of the original string, and
            # subtracting i, which is the number of letters that occured before that
            # letter, we get the number of substrings in that number and add it to
            # the appropriate player's total.

        else:

            stuart += (len(word) - i)

    if kevin > stuart:

        print('Kevin {}'.format(kevin))

    elif kevin < stuart:

        print('Stuart {}'.format(stuart))

    else:

        print('Draw')


if __name__ == '__main__':

    input_word = 'BANANA'
    
    '''
    alternate test case:
    BFEREZKMEYKTNZZTCVZRWZSIIRLEUWGXROAHKC
    RZNZKUUFWEDJVPMGNGDVHNIGUNKDAUFOIYXVMVBNBMLDQAYJSXNJFVZCERKW
    JXYUHHLYEBBVRQTXJMGVNFKYHHPZGZOLIBDNTHTZPDJNASKAQPCTXETRZBGIP
    YHZHOUJPBPRCEKTOWENMEHJVEPPKQISJLTWQOLATVIFOBEXUJPMKXGUDFHBEG
    MFCCUXBJMXFOKRCICSPQQFFJZTIHMLURFCCVZYIPYGDTJXGXSUAHOKLVYFMSH
    OSMNNIIRAUPFAAOQHLQCTUGCMCQMOQUXMYBQXJVYRIIQENPTMBYVOVPFYDOJK
    VUWKDHDWYNVDAMUBBPNTEZZSDADELGNILAZTTMUMWGKXPSQDYVTGXWGDLAZQI
    JADPTFIJSLIDTLEJFJGWMOCPYLAFMVHQHRLGSIQJXQQKJAVBMFKEENTJZWBDT
    DVUBZHVTDFCLLETZJRMYMIQYVWWUOIVPGTNZFNTDKBVZKKFDTSQTVSRAADPWI
    MXEEJHBFRDDDXMOYEHCUHSBWZLHVCKZKUTVWGNTEPYPNGCDMFNKWGARVDMLZJ
    DPIKLWYULIMBOHVOSWZICGZGBKBODQCVIAVTDZQFYLCRWIQBBGMGGERSLPGYA
    SHNYRVVWAVJYASVATKHQNJNYFCUDXKRDNBWHLRIOFVHVFOJQGGAMKNOVDVKJV
    BRNAIUBZQEBPWKXZUCIRQDRTRGWKTYIJZNBRGQYKOAQCPCRKKXPAAHWLKSJUJ
    ZOOIQCSBPDCWHANQPWSIYDBZFCIEWZKYOMMHCHONSOGVMEGGOUKXLGFVOUSIY
    FFLZAPTLJYWIQVXZZPYVTAOQFQURGULWGFKBYIKJOCSITSBFRIJINCOBHGZRS
    XLUZIXHNXFJIJQABSGNQDOAWXIDSSMLPHHQXYJGVXEJVDVJNCLLBDAYUQFDRG
    FAAWMAWZZVDAPLHYDUFYTXFQRFYCIDLXFCASUQAYTHGNBPFT
    '''
    minion_game(input_word)
