# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences: list[str] = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

word_counter: dict[str, int] = {}

words: list[str] = [v.rstrip('?') for v in (' '.join(sentences)).lower().split()]

for word in words:
    word_counter.setdefault(word, 0)
    word_counter[word] += 1

ranking: list[tuple[str, int]] = sorted(word_counter.items(), key=lambda v: v[1], reverse=True)
TOP_RANKING_COUNT = 3

for idx, v in enumerate(ranking[:TOP_RANKING_COUNT]):
    word, encounters = v
    print(f'{idx+1}. "{word}" - {encounters}')

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.
