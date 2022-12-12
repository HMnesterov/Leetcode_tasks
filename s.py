"""
Поликарпу уже надоело получать массивы натуральных чисел на день рождения и
другие праздники. Поэтому его друзья Монокарп и Бикарп решили подарить ему
строки из строчных латинских букв. Как оказалось, Бикарп не очень добросовестно
готовил свой подарок, и две строки могли получиться похожими. Назовем похожестью
строк s и t количество способов представить s как конкатенацию префикса t и суффикса t.
Например, похожесть строк ‘abac’ и ‘abacac’ равна 3, так как ‘abac’ = ‘abac’ + ‘’ = ‘aba’ + ‘c’ = ‘ab’ + ‘ac’.
Поликарп хочет узнать похожесть своих подарков и попросил вас сделать это за него,
ак как сейчас он все еще принимает гостей.

Замечание
похожесть строк s и t не всегда равна похожести строк t и s.

Пример 1
Входные данные:
abac
abacac

Выходные данные:
3
"""

s = input()
t = input()
if s == t:
    print(len(s) + 1)
    exit()
count = 0
len_s = len(s)
len_t = len(t)
for z in range(len_s + 1):
    first_part = t[:z]
    second_part = t[len_t - (len_s - len(first_part)):]


    if first_part + second_part == s:
        count += 1
print(count)
