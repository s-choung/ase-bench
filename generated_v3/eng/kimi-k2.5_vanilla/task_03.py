from ase.build import mx2

atoms = mx2(formula='MoS2')
atoms.cell[2, 2] = atoms.positions[:, 2].ptp() + 10.0
atoms.center(axis=2)
print(atoms.cell)
