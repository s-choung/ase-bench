from ase import Atoms
from ase.data import chemical_symbols, atomic_numbers
from ase.data import covalent_radii
from ase.lattice import crystal
from ase.db import connect
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import read

# Retrieve CH4 from ASE G2 database
db = connect('g2.db')
entries = db.select('formula', 'CH4')
if not entries:
    raise ValueError("CH4 not found in G2 database")
data = entries[0]

# Create Atoms object from retrieved data
atoms = Atoms(cell=data.cell,
               numbers=data.numbers,
               positions=data.positions,
               pbc=True)

# Print atomic coordinates
print("Atomic Coordinates:")
for atom in atoms:
    print(f"{chemical_symbols[atom.number]:<3}{atom.position}")

# Calculate bond lengths
bond_lengths = []
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        if atoms[i].number == 1 and atoms[j].number == 6:  # C-H bond
            bond_lengths.append(atoms.distance(i, j))

print("\nBond Lengths (Angstroms):")
print(bond_lengths)

# Print chemical formula
chemical_formula = ''.join([chemical_symbols[atom.number] for atom in atoms])
print(f"\nChemical Formula: {chemical_formula}")
