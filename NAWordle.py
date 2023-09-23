from tkinter import* # Библиотека # Fylhtq
m = Tk()
wd, hg = 1350, 800 # Размеры окна
c = Canvas(width = wd, height = hg, bg = '#000000') # Окно
m.title('Викторина по математике') # Название окна


from random import randint # Добавление рандома
import time # Добавление времени
words = open ('NACkjdma.txt','r').readlines() # Список слов
quests = open ('NACkjdmaqu.txt','r').readlines() # Список слов и заданий

nw = len(words) # Длина списка
nsn = 6 # Длина слова в начале
nsm = 3 # Минимальная длина слова
nsb = 18 # Максимальная длина слова
w = randint(0, nw - 1) # Рандомный выбор неизвестного слова
nsw = len(words[w]) - 1 # Длина неизвестного слова
hr = 0 # Начало задания
while quests[w][hr] != '#' :
    hr = hr + 1
t = 0 # Номер введённой буквы
k = 6 # Количество попыток
u = 0 # Проверка позиции буквы
g = 0 # Номер попытки
p = 0 # Положение страницы
s = 0 # Проверка существования слова
r = 30 # Размер текста
d = 60 # Размер ячейки
f = 10 # Расстояние между ячейками
xt = 50 # Отступ с края
yt = d + 2*f # Отступ с края
fo = 'Courier New' # Шрифт
tc = time.perf_counter() # Начало отсчёта
q = []
def place_word(word, colors, font, x, y) : # Текст
    for i in range(0, len(word), 1) :
        c.create_text(x + i*font*1.2, y, font = (fo, font), fill = colors[i], text = word[i])
        c.pack()

c.create_rectangle(xt, f, xt + (nsb - 1)*f + nsb*d, d + f, fill = '#F5E1F8', outline = '#F5E1F8')

if int((wd - 2*xt) / 1.2 / (len(quests[w]) - hr)) < 24 : # Шрифт задания
    place_word(quests[w][hr:len(quests[w])], ['#BE0CE6']*(len(quests[w]) - hr), int((wd - 2*xt) / 1.2 / (len(quests[w]) - hr)), 60, 34)
else :
    place_word(quests[w][hr:len(quests[w])], ['#BE0CE6']*(len(quests[w]) - hr), 24, 60, 34)

word = ['А']*nsn # Изначальный вид слова

for i in range(nsn) : # Создание ячеек
    for j in range(k) :
        c.create_rectangle(xt + (d + f)*i, yt + (d + f)*j, (xt + d) + (d + f)*i, (yt + d) + (d + f)*j, fill = '#F5E1F8', outline = '#F5E1F8')

c.create_rectangle(xt, yt + k*(d + f), xt + (nsn - 1)*f + nsn*d, yt + k*(d + f) + d, fill = '#F5E1F8', outline = '#F5E1F8')

def operation (l) : # Ввод буквы
    global t, g, u, s, nsn, nsw, nw, words, word, w, q, tc
    if g < k :
        word[t] = l
        place_word(word[t], ['#000000'], r, (xt + int(d / 2)) + (d + f)*t, yt + int(d / 2) + (d + f)*k)
        t = t + 1
        if t == nsn :
            t = 0
            c.create_rectangle(xt, yt + k*(d + f), xt + (nsn - 1)*f + nsn*d, yt + k*(d + f) + d, fill = '#F5E1F8', outline = '#F5E1F8')
            for h in range (nw) :
                q = []
                for i in range (nsn) :
                    if len (words[h]) - 1 == nsn :
                        q = q + [words[h][i]]
                        if q == word :
                            s = 1
            if s != 0 :
                s = 0
                for i in range (nsn) :
                    place_word(word[i], ['#000000'], r, xt + r + (d + f)*i, yt + r + (d + f)*g)
                    for j in range (nsw) :
                        if word[i] == words[w][j] :
                            u = u + 1
                        if u != 0 :
                            u = 0
                            place_word(word[i], ['#1890CC'], r, xt + r + (d + f)*i, yt + r + (d + f)*g)
                    if nsn == nsw :
                        if word[i] == words[w][i]:
                            place_word(word[i], ['#BE0CE6'], r, xt + r + (d + f)*i, yt + r + (d + f)*g)
                g = g + 1
                q = []
                for i in range (nsw) :
                        q = q + [words[w][i]]
                if g == k or word[0:nsn] == q :
                    g = k
                    clock(tc)
                    c.create_rectangle(xt, yt + k*(d + f), xt + (nsb - 1)*f + nsb*d, yt + k*(d + f) + d, fill = '#000000', outline = '#000000')
                    c.create_rectangle(xt, yt + k*(d + f), xt + (nsw - 1)*f + nsw*d, yt + k*(d + f) + d, fill = '#F5E1F8', outline = '#F5E1F8')
                    for i in range (nsw) :
                        place_word(words[w][i], ['#BE0CE6'], r, (xt + int(d / 2)) + (d + f)*i, yt + int(d / 2) + (d + f)*k)
    return t, g, word

def operation_q (coordinates1) : # Ввод буквы
    operation('Й')

def operation_w (coordinates2) :
    operation('Ц')

def operation_e (coordinates3) :
    operation('У')

def operation_r (coordinates4) :
    operation('К')

def operation_t (coordinates5) :
    operation('Е')

def operation_y (coordinates6) :
    operation('Н')

def operation_u (coordinates7) :
    operation('Г')

def operation_i (coordinates8) :
    operation('Ш')

def operation_o (coordinates9) :
    operation('Щ')

def operation_p (coordinates10) :
    operation('З')

def operation_ch (coordinates11) :
    operation('Х')

def operation_iu (coordinates12) :
    operation('Ъ')

def operation_a (coordinates13) :
    operation('Ф')

def operation_s (coordinates14) :
    operation('Ы')

def operation_d (coordinates15) :
    operation('В')

def operation_f (coordinates16) :
    operation('А')

def operation_g (coordinates17) :
    operation('П')

def operation_h (coordinates18) :
    operation('Р')

def operation_j (coordinates19) :
    operation('О')

def operation_k (coordinates20) :
    operation('Л')

def operation_l (coordinates21) :
    operation('Д')

def operation_dz (coordinates22) :
    operation('Ж')

def operation_ea (coordinates23) :
    operation('Э')

def operation_z (coordinates24) :
    operation('Я')

def operation_x (coordinates25) :
    operation('Ч')

def operation_c (coordinates26) :
    operation('С')

def operation_v (coordinates27) :
    operation('М')

def operation_b (coordinates28) :
    operation('И')

def operation_n (coordinates29) :
    operation('Т')  

def operation_m (coordinates30) :
    operation('Ь')

def operation_bp (coordinates31) :
    operation('Б')

def operation_yu (coordinates32) :
    operation('Ю')

def operation_yo (coordinates33) :
    operation('Ё')

def back (coordinates34) : # Удаление буквы
    global t
    if t != 0 :
        t = t - 1
        c.create_rectangle(xt + t*(d + f), yt + k*(d + f), xt + t*(d + f) + d, yt + k*(d + f) + d, fill = '#F5E1F8', outline = '#F5E1F8')

def pageup (coordinates35) : # Пролистывание страницы вверх
    global p
    p = p - 1
    c.create_rectangle(xt, yt + 7*(d + f), xt + 10*d + 9*f, hg - f, fill = '#F5E1F8', outline = '#F5E1F8')
    place_word(words[p][0:len(words[p])], ['#969696']*len(words[p]), r, 84, 610)
    place_word(words[p + 1][0:len(words[p + 1])], ['#000000']*len(words[p + 1]), r, 84, 680)
    place_word(words[p + 2][0:len(words[p + 2])], ['#969696']*len(words[p + 2]), r, 84, 750)

def pagedown (coordinates36) : # Пролистывание страницы вниз
    global p
    p = p + 1
    c.create_rectangle(xt, yt + 7*(d + f), xt + 10*d + 9*f, hg - f, fill = '#F5E1F8', outline = '#F5E1F8')
    place_word(words[p][0:len(words[p])], ['#969696']*len(words[p]), r, 84, 610)
    place_word(words[p + 1][0:len(words[p + 1])], ['#000000']*len(words[p + 1]), r, 84, 680)
    place_word(words[p + 2][0:len(words[p + 2])], ['#969696']*len(words[p + 2]), r, 84, 750)

def page (txt) : # Поиск в списке по букве
    p = 0
    while txt != words[p][0] :
        p = p + 1
    c.create_rectangle(xt, yt + 7*(d + f), xt + 10*d + 9*f, hg - f, fill = '#F5E1F8', outline = '#F5E1F8')
    place_word(words[p][0:len(words[p])], ['#969696']*len(words[p]), r, 84, 610)
    place_word(words[p + 1][0:len(words[p + 1])], ['#000000']*len(words[p + 1]), r, 84, 680)
    place_word(words[p + 2][0:len(words[p + 2])], ['#969696']*len(words[p + 2]), r, 84, 750)
    return p

def operation_alt_q (coordinates37) : # Поиск в списке по букве
    global p
    p = page('Й')

def operation_alt_w (coordinates38) :
    global p
    p = page('Ц')

def operation_alt_e (coordinates39) :
    global p
    p = page('У')

def operation_alt_r (coordinates40) :
    global p
    p = page('К')

def operation_alt_t (coordinates41) :
    global p
    p = page('Е')

def operation_alt_y (coordinates42) :
    global p
    p = page('Н')

def operation_alt_u (coordinates43) :
    global p
    p = page('Г')

def operation_alt_i (coordinates44) :
    global p
    p = page('Ш')

def operation_alt_o (coordinates45) :
    global p
    p = page('Щ')

def operation_alt_p (coordinates46) :
    global p
    p = page('З')

def operation_alt_ch (coordinates47) :
    global p
    p = page('Х')

def operation_alt_iu (coordinates48) :
    global p
    p = page('Ъ')

def operation_alt_a (coordinates49) :
    global p
    p = page('Ф')

def operation_alt_s (coordinates50) :
    global p
    p = page('Ы')

def operation_alt_d (coordinates51) :
    global p
    p = page('В')

def operation_alt_f (coordinates52) :
    global p
    p = page('А')

def operation_alt_g (coordinates53) :
    global p
    p = page('П')

def operation_alt_h (coordinates54) :
    global p
    p = page('Р')

def operation_alt_j (coordinates55) :
    global p
    p = page('О')

def operation_alt_k (coordinates56) :
    global p
    p = page('Л')

def operation_alt_l (coordinates57) :
    global p
    p = page('Д')

def operation_alt_dz (coordinates58) :
    global p
    p = page('Ж')

def operation_alt_ea (coordinates59) :
    global p
    p = page('Э')

def operation_alt_z (coordinates60) :
    global p
    p = page('Я')

def operation_alt_x (coordinates61) :
    global p
    p = page('Ч')

def operation_alt_c (coordinates62) :
    global p
    p = page('С')

def operation_alt_v (coordinates63) :
    global p
    p = page('М')

def operation_alt_b (coordinates64) :
    global p
    p = page('И')

def operation_alt_n (coordinates65) :
    global p
    p = page('Т')

def operation_alt_m (coordinates66) :
    global p
    p = page('Ь')

def operation_alt_bp (coordinates67) :
    global p
    p = page('Б')

def operation_alt_yu (coordinates68) :
    global p
    p = page('Ю')

def operation_alt_yo (coordinates69) :
    global p
    p = page('Ё')

def vinput (coordinates70) : # Выбор слова из списка
    global word, words, nsn, p, t, g, d, f, xt, yt, word
    if g < k :
        c.create_rectangle(xt, yt + k*(d + f), xt + (nsb - 1)*f + nsb*d, yt + k*(d + f) + d, fill = '#000000', outline = '#000000')
        while t > 0 :
            t = t - 1
            c.create_rectangle(xt + (d + f)*t, yt + k*(d + f), (xt + d) + (d + f)*t, yt + k*(d + f) + d, fill = '#F5E1F8', outline = '#F5E1F8')
        nsn = nsb
        c.create_rectangle(xt, (yt + d + f) + (d + f)*(g - 1), (xt + d) + (d + f)*(nsn - 1), (yt + d) + (d + f)*(k - 1), fill = '#000000')
        nsn = len(words[p + 1]) - 1
        word = ['А']*nsn
        for i in range(nsn) :
            for j in range(g, k) :
                c.create_rectangle(xt + (d + f)*i, yt + (d + f)*j, (xt + d) + (d + f)*i, (yt + d) + (d + f)*j, fill = '#F5E1F8', outline = '#F5E1F8')
        word[0:nsn] = words[p + 1][0:nsn]
        for i in range (nsn) :
            operation (word[i])

def left (coordinates71) : # Уменьшение слова
    global nsn, nsm, nsw, nw, xt, yt, d, f, k, t, g, u, s, w, q, word, tc
    if nsn > nsm and g < k :
        c.create_rectangle(xt, (yt + d + f) + (d + f)*(g - 1), (xt + d) + (d + f)*(nsn - 1), (yt + d) + (d + f)*(k - 1), fill = '#000000')
        nsn = nsn - 1
        c.create_rectangle(xt + (nsn - 1)*(d + f) + d, yt + k*(d + f), xt + nsn*(d + f) + d, yt + k*(d + f) + d, fill = '#000000', outline = '#000000')
        word = word[0:nsn]
        for i in range(nsn) :
            for j in range(g, k) :
                c.create_rectangle(xt + (d + f)*i, yt + (d + f)*j, (xt + d) + (d + f)*i, (yt + d) + (d + f)*j, fill = '#F5E1F8', outline = '#F5E1F8')
        if t == nsn :
            t = 0
            c.create_rectangle(xt, yt + k*(d + f), xt + (nsn - 1)*f + nsn*d, yt + k*(d + f) + d, fill = '#F5E1F8', outline = '#F5E1F8')
            for h in range (nw) :
                q = []
                for i in range (nsn) :
                    if len (words[h]) - 1 == nsn :
                        q = q + [words[h][i]]
                        if q == word :
                            s = 1
            if s != 0 :
                s = 0
                for i in range (nsn) :
                    place_word(word[i], ['#000000'], r, xt + r + (d + f)*i, yt + r + (d + f)*g)
                    for j in range (nsw) :
                        if word[i] == words[w][j] :
                            u = u + 1
                        if u != 0 :
                            u = 0
                            place_word(word[i], ['#1890CC'], r, xt + r + (d + f)*i, yt + r + (d + f)*g)
                    if nsn == nsw :
                        if word[i] == words[w][i]:
                            place_word(word[i], ['#BE0CE6'], r, xt + r + (d + f)*i, yt + r + (d + f)*g)
                g = g + 1
                q = []
                for i in range (nsw) :
                        q = q + [words[w][i]]
                if g == k or word[0:nsn] == q :
                    g = k
                    clock(tc)
                    c.create_rectangle(xt, yt + k*(d + f), xt + (nsb - 1)*f + nsb*d, yt + k*(d + f) + d, fill = '#000000', outline = '#000000')
                    c.create_rectangle(xt, yt + k*(d + f), xt + (nsw - 1)*f + nsw*d, yt + k*(d + f) + d, fill = '#F5E1F8', outline = '#F5E1F8')
                    for i in range (nsw) :
                        place_word(words[w][i], ['#BE0CE6'], r, (xt + int(d / 2)) + (d + f)*i, yt + int(d / 2) + (d + f)*k)

def right (coordinates72) : # Увеличение слова
    global nsn, nsb, xt, yt, d, f, k, t, word
    if nsn < nsb and g < k :
        nsn = nsn + 1
        c.create_rectangle(xt + (nsn - 2)*(d + f) + d, yt + k*(d + f), xt + (nsn - 1)*(d + f) + d, yt + k*(d + f) + d, fill = '#F5E1F8', outline = '#F5E1F8')
        word = word + ['A']
        for i in range(nsn) :
            for j in range(g, k) :
                c.create_rectangle(xt + (d + f)*i, yt + (d + f)*j, (xt + d) + (d + f)*i, (yt + d) + (d + f)*j, fill = '#F5E1F8', outline = '#F5E1F8')

def clock (tc) : # Прошедшее время
    c.create_rectangle(xt + 10*(d + f), yt + 7*(d + f), wd - xt, hg - f, fill = '#F5E1F8', outline = '#F5E1F8')
    tcn = time.perf_counter()
    tn = int(tcn - tc)
    tns = tn % 60
    tnm = int(tn / 60)
    if len(str(tns)) == 1 :
        tns = str('0' + str(tns))
    else :
        tns = str(tns)
    if len(str(tnm)) == 1 :
        tnm = str('0' + str(tnm))
    else :
        tnm = str(tnm)
    strk = tnm, ':', tns
    place_word(strk, ['#BE0CE6']*len(strk), 80, 932, 680)

page('А') # Начальная позиция списка

c.bind_all('<q>', operation_q) # Функции клавиш
c.bind_all('<w>', operation_w)
c.bind_all('<e>', operation_e)
c.bind_all('<r>', operation_r)
c.bind_all('<t>', operation_t)
c.bind_all('<y>', operation_y)
c.bind_all('<u>', operation_u)
c.bind_all('<i>', operation_i)
c.bind_all('<o>', operation_o)
c.bind_all('<p>', operation_p)
c.bind_all('<[>', operation_ch)
c.bind_all('<]>', operation_iu)
c.bind_all('<a>', operation_a)
c.bind_all('<s>', operation_s)
c.bind_all('<d>', operation_d)
c.bind_all('<f>', operation_f)
c.bind_all('<g>', operation_g)
c.bind_all('<h>', operation_h)
c.bind_all('<j>', operation_j)
c.bind_all('<k>', operation_k)
c.bind_all('<l>', operation_l)
c.bind_all('<;>', operation_dz)
c.bind_all("<'>", operation_ea)
c.bind_all('<z>', operation_z)
c.bind_all('<x>', operation_x)
c.bind_all('<c>', operation_c)
c.bind_all('<v>', operation_v)
c.bind_all('<b>', operation_b)
c.bind_all('<n>', operation_n)
c.bind_all('<m>', operation_m)
c.bind_all('<,>', operation_bp)
c.bind_all('<.>', operation_yu)
c.bind_all('<`>', operation_yo)
c.bind_all('<Delete>', back)
c.bind_all('<Up>', pageup)
c.bind_all('<Down>', pagedown)
#c.bind_all('<Alt-q>', operation_alt_q)
c.bind_all('<Alt-w>', operation_alt_w)
c.bind_all('<Alt-e>', operation_alt_e)
c.bind_all('<Alt-r>', operation_alt_r)
#c.bind_all('<Alt-t>', operation_alt_t)
c.bind_all('<Alt-y>', operation_alt_y)
c.bind_all('<Alt-u>', operation_alt_u)
c.bind_all('<Alt-i>', operation_alt_i)
c.bind_all('<Alt-o>', operation_alt_o)
c.bind_all('<Alt-p>', operation_alt_p)
c.bind_all('<Alt-[>', operation_alt_ch)
#c.bind_all('<Alt-]>', operation_alt_iu)
c.bind_all('<Alt-a>', operation_alt_a)
#c.bind_all('<Alt-s>', operation_alt_s)
c.bind_all('<Alt-d>', operation_alt_d)
c.bind_all('<Alt-f>', operation_alt_f)
c.bind_all('<Alt-g>', operation_alt_g)
c.bind_all('<Alt-h>', operation_alt_h)
c.bind_all('<Alt-j>', operation_alt_j)
c.bind_all('<Alt-k>', operation_alt_k)
c.bind_all('<Alt-l>', operation_alt_l)
#c.bind_all('<Alt-;>', operation_alt_dz)
c.bind_all("<Alt-'>", operation_alt_ea)
c.bind_all('<Alt-z>', operation_alt_z)
c.bind_all('<Alt-x>', operation_alt_x)
c.bind_all('<Alt-c>', operation_alt_c)
c.bind_all('<Alt-v>', operation_alt_v)
c.bind_all('<Alt-b>', operation_alt_b)
c.bind_all('<Alt-n>', operation_alt_n)
#c.bind_all('<Alt-m>', operation_alt_m)
c.bind_all('<Alt-,>', operation_alt_bp)
#c.bind_all('<Alt-.>', operation_alt_yu)
#c.bind_all('<Alt-`>', operation_alt_yo)
c.bind_all('<Return>', vinput)
c.bind_all('<Left>', left)
c.bind_all('<Right>', right)

m.mainloop()
