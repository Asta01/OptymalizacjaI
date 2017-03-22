# sagepython
# (1,2) (1,4) (2,6) (3,8)
# (2,1) (4,1) (5,2) (5,3)

lp = MixedIntegerLinearProgram(maximization=True)
x = lp.new_variable(nonnegative=False)

lp.set_objective(0)

lp.add_constraint( x[1] + 2 * x[2] + x[3] >= d)
lp.add_constraint( x[1] + 4 * x[2] + x[3] >= d)
lp.add_constraint( 2 * x[1] + x[2] + x[3] >= d)
lp.add_constraint( 3 * x[1] + 8 * x[2] + x[3] >= d)

lp.add_constraint( -2 * x[1] - x[2] - x[3] >= d)
lp.add_constraint( -4 * x[1] - x[2] - x[3] >= d)
lp.add_constraint( -5 * x[1] - x[2] + x[3] >= d)
lp.add_constraint( 3 * x[1] + 8 * x[2] + x[3] >= d)

print lp.solve()

wartosci = lp.get_vqalues(a)
print wartosci



# punkty czarne

C1 = (1,1)
C2 = (1,2)
C3 = (1,3)
C = [ C1 , C2 , C3 ]

# punkty białe

B1 = (2,1)
B2 = (3,1)
B3 = (4,1)

B = [ B1 , B2 , B3 ]

p = MixedIntegerLinearProgram(maximization=True)
var = p.new_variable(nonnegative=True)

A, D, d = var[ 'A' ] , var[ 'D' ], var[ 'd' ]

p.set_objective(0)


#szukamy A,D takich, żeby Ax+B oddzielała punkty białe od czarnych

p.add_constraint( d > 0 )

for c in C:
    p.add_constraint(A * c[0] + D - c[1] < d )
    
for b in B:
    p.add_constraint(-A * b[0] - D + b[1] < d )
    
    
print p.get_values(A)
print p.get_values(D)

