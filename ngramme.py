def ngramme(wort, n):
    """Erzeugt aus einem gegebenen Wort die Liste aller n-Gramme.

    Ist ein Generator.
    
    >>> ngramme('hallowelt', 3)
    ['hal', 'all', 'llo', 'low', 'owe', 'wel', 'elt']
    >>> ngramme('hallowelt', 4)
    ['hall', 'allo', 'llow', 'lowe', 'owel', 'welt']
    >>> ngramme('dodo', 10)
    ['dodo']
    """

    if len(wort) < n:
        yield wort
        return

    ngram = wort[0:n]
    yield ngram

    for char in wort[n:]:
        ngram = ngram[1:] + char
        yield ngram

    return

def scoreGen(wortliste, n):
    scoretable = {}
    for wort in wortliste:
        ngramm = ngramme(wort,n)
        for ng in ngramm:
            scoretable[ng] = 1 + scoretable.get(ng,0)
    return scoretable

def score(n, wort, wortliste):
    st = scoreGen(wortliste, n)

    score = 0
    for ngram in ngramme(wort, n):
        score += st.get(ngram, 0)

    return score

klein = []
gross = []


file0 = open('wordlisteDeutschGross.txt','r')
wortlisteGross = file0.read()
file0.close()
file1 = open('wordlisteDeutschKlein.txt','r')
wortlisteKlein = file1.read()
file1.close()

klein =  wortlisteKlein.split('\n')
gross = wortlisteGross.split('\n')


def search(character):
	if ord(character) in range(65,92):
		return gross[ord(character)-65]
	elif ord(character) in range(97,123):
		return klein[ord(character)-97]

testString = 'Buecherregel'
print score(3,testString,klein)
