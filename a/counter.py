import operator


def count(article):
    word = article.split()
    word_count = len(word)
    d = {}
    for ch in word:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    val = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    return val, word_count
