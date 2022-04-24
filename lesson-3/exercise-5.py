import random


NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat_world=False):
    '''
   Makes some random jokes.
    '''

    jokes = []
    if not repeat_world:
        nouns_copy = NOUNS.copy()
        random.shuffle(nouns_copy)
        adverbs_copy = ADVERBS.copy()
        random.shuffle(adverbs_copy)
        adjectives_copy = ADJECTIVES.copy()
        random.shuffle(adjectives_copy)
        for num, (noun, adverb, adjective) in enumerate(zip(nouns_copy, adverbs_copy, adjectives_copy)):
            jokes.append(f'{noun} {adjective} {adverb}')
            if num == n:
                break
    else:
        for _ in range(n):
            jokes.append(f'{random.choice(NOUNS)} {random.choice(ADVERBS)} {random.choice(ADJECTIVES)}')
    return jokes
count = int(input('Введите желаемое число шуток:\n'))

print(f'Создание шутки:\n {get_jokes(count)}')
