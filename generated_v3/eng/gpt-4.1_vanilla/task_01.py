from ase.build import bulk, make_supercell

a = bulk('Cu', 'fcc', a=3.61)
P = [[2,0,0],[0,2,0],[0,0,2]]
s = make_supercell(a, P)
print("Cell:\n", s.cell)
print("Number of atoms:", len(s))
