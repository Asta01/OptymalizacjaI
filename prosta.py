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
