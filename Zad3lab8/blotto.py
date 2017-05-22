# Gra zaklada liczbe dostepnych zolnierzy rowna 6 oraz pozwala na wysylanie pustych oddzialow oraz dowolna kolejnosc wysylania oddzialow.
# W ten sposob mamy dostepne 28 mozliwych strategii:
s1 = [[0,0,6],[0,6,0],[6,0,0]]
s2 = [[0,1,5],[0,5,1],[1,0,5],[1,5,0],[5,0,1],[5,1,0]]
s3 = [[0,2,4],[0,4,2],[2,0,4],[2,4,0],[4,0,2],[4,2,0]]
s4 = [[0,3,3],[3,0,3],[3,3,0]]
s5 = [[1,1,4],[1,4,1],[4,1,1]]
s6 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
s7 = [[2,2,2]]

# utozsamiamy ze soba strategie tak jak powyzej, w ten sposob mamy 7 strategii {s1,s2,s3,s4,s5,s6,s7}
lista = [s1,s2,s3,s4,s5,s6,s7]

# wylicza czy pojedyncza strategia A1 wygrywa(zwraca 1), remisuje(0) czy przegrywa(-1) ze strategią A2
def wynik(A1,A2):
    k=0.0
    for i in range(len(A1)):
        if A1[i]>A2[i]:
            k = k+1
        if A1[i]<A2[i]:
            k = k-1
    return k

#wylicza wielkosc wygranej strategii s1 ze strategia s2
def wygrana(s1,s2):
    k=0.0
    for i in s1:
        for j in s2:
            k = k + wynik(i,j)
    return k/(len(s1)*len(s2))

#tworzymy macierz wyplaty
M=[]
for i in range(len(lista)):
    N = []
    for j in range(len(lista)):
         N.append(wygrana(lista[i],lista[j]))
    print(N)
    M.append(N)

#obliczamy strategie optymalna
p = MixedIntegerLinearProgram(maximization=True)
v = p.new_variable(real=True)

p.set_objective(v[0])

for i in range (len(M)):
    p.add_constraint(v[0] <= M[0][i]*v[1] + M[1][i]*v[2] + M[2][i]*v[3] + M[3][i]*v[4] + M[4][i]*v[5] + M[5][i]*v[6] + M[6][i]*v[7])
p.add_constraint(1 <= v[1] + v[2] + v[3] + v[4] + v[5] + v[6] + v[7] <= 1)
p.add_constraint(0 <= v[1])
p.add_constraint(0 <= v[2])
p.add_constraint(0 <= v[3])
p.add_constraint(0 <= v[4])
p.add_constraint(0 <= v[5])
p.add_constraint(0 <= v[6])
p.add_constraint(0 <= v[7])

p.solve()
p.show()

x = [p.get_values(v[1]),p.get_values(v[2]),p.get_values(v[3]),p.get_values(v[4]),p.get_values(v[5]),p.get_values(v[6]),p.get_values(v[7])]

print('Optymalna strategia gracza to ' + str(x) + '.')
# wynik to tak naprawde [0,0,0,3/7,3/7,1/7], to, co pokazuje program uwzglednia bledy obliczeniowe
