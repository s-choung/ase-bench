from ase import Atoms
from ase.build import molecule, bulk
from ase.calculators.emt import EMT
from ase.vasp import Poscar

# Build Al(111) slab
al_slab = bulk('Al', 'fcc', a=4.05, size=(1, 1, 4), center=True)
al_slab = al_slab.repeat((3, 3, 1))

# Create N2 molecule
n2 = molecule('N2', a=1.1)

# Define lattice vectors to match aluminum
n2.set_cell(al_slab.cell)

# Place N2 on the bridge site of the Al(111) slab
n2.position = [1/3, 2/3, 2.0]

# Add molecule to the slab and set vacuum
final_structure = al_slab + n2 + [n2] + al_slab * 10
final_structure.center(axis=(2,))

# Print the number of atoms and atom types in the final structure
print(f'Number of atoms in final structure: {len(final_structure)}')
print(f'Number of atom types: {len(set(final_structure.get_chemical_symbols()))}')
