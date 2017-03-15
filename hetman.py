def hetman(n):
    print ' \* Problem: hetman *\ '
    print
    print 'Maximize'
    out = ''

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            out += 'x' + str(i) + str(j) + ' + '

    print out[:-3]
    print
    print 'Subject to'

    # poziom
    for i in range(1, n + 1):
        out = ''
        for j in range(1, n + 1):
            out += 'x' + str(i) + str(j) + ' + '
        print out[:-3] + ' <= 1'

    # pion
    for i in range(1, n + 1):
        out = ''
        for j in range(1, n + 1):
            out += 'x' + str(j) + str(i) + ' + '
        print out[:-3] + ' <= 1'

    # skos w prawo dolny
    for i in range(n-1, 1, -1):
        x = i
        y = 1
        out = ''
        for j in range(1, n-i+2):
            out += 'x' + str(x) + str(y) + ' + '
            x += 1
            y += 1
        print out[:-3] + ' <= 1'

    # glowna przekatna w prawo
    out = ''
    for i in range(1, n+1):
        out += 'x' + str(i) + str (i) + ' + '
    print out[:-3] + ' <= 1'

    # skos w prawo gorny
    for i in range(n-1, 1, -1):
        x = i
        y = 1
        out = ''
        for j in range(1, n-i+2):
            out += 'x' + str(y) + str(x) + ' + '
            x += 1
            y += 1
        print out[:-3] + ' <= 1'

    # skos w lewo dolny
    for i in range(n - 1, 1, -1):
        x = i
        y = n
        out = ''
        for j in range(1, n - i + 2):
            out += 'x' + str(x) + str(y) + ' + '
            x += 1
            y -= 1
        print out[:-3] + ' <= 1'

    # glowna przekatna w lewo
    x = 1
    y = n
    out = ''
    for i in range(1, n + 1):
        out += 'x' + str(x) + str(y) + ' + '
        x += 1
        y -= 1
    print out[:-3] + ' <= 1'

    # skos w prawo gorny
    for i in range(2, n):
        x = i
        y = 1
        out = ''
        for j in range(1, i + 1):
            out += 'x' + str(y) + str(x) + ' + '
            x -= 1
            y += 1
        print out[:-3] + ' <= 1'

    print
    print 'Bounds'

    for i in range(1,n+1):
        for j in range(1,n+1):
            print '0 <= x' + str(i) + str(j) + ' <= 1'

    print
    print 'Generals'

    for i in range(1,n+1):
        for j in range(1,n+1):
            print 'x' + str(i) + str(j)

    print
    print 'End'


n = raw_input('Podaj rozmiar szachownicy: ')
n = int(n)
hetman(n)
