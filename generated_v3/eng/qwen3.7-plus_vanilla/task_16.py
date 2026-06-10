from ase.build import surface

atoms = surface('bcc', 'Fe', (1, 1, 0), layers=4, vacuum=10.0)

# Apply size. Note: z=1 is used to preserve the requested 4 layers. 
# (Using z=4 would stack 4 identical slabs, resulting in 16 layers).
atoms *= (2, 2, 1)

print(len(atoms))
print(atoms.cell.cellpar())
