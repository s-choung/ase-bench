from ase.build import mx2, add_vacuum

atoms = mx2('MoS2', kind='2H', vacuum=0)
add_vacuum(atoms, 10.0)
print(atoms.cell.lengths())
