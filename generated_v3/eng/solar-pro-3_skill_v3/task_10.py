from ase.cluster import Octahedron

atoms = Octahedron('Cu', length=5)  # size ~5 Bohr (typical default unit)
atoms.calc = None                 # no calculator needed for printing

print('Number of atoms:', len(atoms))
print('Positions shape:', atoms.positions.shape)
