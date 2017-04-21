p = MixedIntegerLinearProgram(maximization=False)
v = p.new_variable(real=True, nonnegative=True)

liczba_zmiennych = int(raw_input('Podaj liczbe zmiennych:'))
liczba_ograniczen = int(raw_input('Podaj liczbe ograniczen:'))

print('Uwaga:')
print('Program zakłada, że ograniczenia programu są wpisywane w postaci: a*v[1] + b*v[2] <= c')
print('W powyższym zapisie zmieniać można tylko współczynniki a,b,c itd.')
for i in range(1, liczba_ograniczen + 1):
    k = liczba_zmiennych + i
    s = raw_input('Podaj ograniczenie nr ' + str(i) + ': ')
    s = s.replace('<=', '+ v[' + str(k) + '] ==')
    code = parser.expr(s).compile()
    p.add_constraint(eval(code))

s = ''
for i in range(1, liczba_ograniczen + 1):
    s = s + 'v[' + str(liczba_zmiennych + i) + '] + '
s = s[:-3]
code = parser.expr(s).compile()
p.set_objective(eval(code))

p.show()

print('Objective Value: {}'.format(p.solve()))
for i, v in p.get_values(v).iteritems():
    print('v_' + str(i) + ' = ' + str(int(round(v))))
if p.solve < 0 :
    print('Oryginalny problem jest sprzeczny.')
