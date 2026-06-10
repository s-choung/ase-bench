from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT

# Create Au icosahedron nanoparticle
atoms = bulk('Au', crystalstructure='fcc', a=4.0, cubic=True)
atoms = Atoms(numbers=atoms.numbers, positions=atoms.get_positions()-atoms.get_center_of_mass())

# Add icosahedron vertices
vertices = atoms.positions[[1, 2, 3, 4, 7, 11, 12, 13, 16, 17, 20, 21, 23, 26, 28, 29, 31, 34, 35, 36]]
atoms.extend(Atoms('Au', positions=vertices))

# Add more shells
for i in range(2):
    atoms.extend(Atoms('Au', positions=vertices))

atoms.wrap()
atoms.set_calculator(EMT())

# Print number of atoms and center of mass
print(f'Number of atoms: {len(atoms)}')
print('Center of Mass:', atoms.get_center_of_mass())
