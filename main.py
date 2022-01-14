import pandas
pf = pandas.read_csv("nato_phonetic_alphabet.csv")
ef = {r.letter: r.code for (i, r) in pf.iterrows()}
# print(pf.to_dict())

def genr():
    ab = input("What's your name?: ").upper()
    try:
        op = [ef[i] for i in ab]
    except KeyError:
        print("Sorry, Only letters in the alphabet please")
        genr()
    else:
        print(op)

genr()





