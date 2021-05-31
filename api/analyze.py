from jlpt import jlpt_kanji

def analyzeText(text):
    unique_kanji = {level : set() for level in range(1, 6)}
    for line in text:
        for c in line:
            #print(len(c))
            for level in range(1, 6):
                if c in jlpt_kanji[level]:
                    unique_kanji[level].add(c)
    #unique_kanji_count = {level : len(unique_kanji[level]) for level in range(1, 6)}
    #n5 to n1
    unique_kanji_count = [len(unique_kanji[level]) for level in reversed(range(1, 6))]
    return {'unique kanji count' : unique_kanji_count}