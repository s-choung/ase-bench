from ase.build import bulk

cu = bulk('Cu', 'fcc', a=3.615)
supercell = cu.repeat((2, 2, 2))

print("Primitive cell:")
print(cu.cell)
print("Number of atoms:", len(cu))

print("\n2x2x2 supercell:")
print(supercell.cell)
print("Number of atoms:", len(supercell))
