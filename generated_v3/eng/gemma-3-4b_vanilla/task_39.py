from ase import Atoms
from ase.calculators.emt import EMT
from ase.io import write, read

# Create Au FCC bulk
elements = {'Au': 1}
lattice = 4.086  # Angstrom
atoms = Atoms('Au', positions=[(0, 0, 0), (1, 0, 0), (1/2, 1/2, 0), (0, 1/2, 0), (1/2, 1/2, 1), (0, 1/2, 1)], cell=[[lattice, 0, 0], [0, lattice, 0], [0, 0, lattice]])

# Perform EMT calculation
calc = EMT()
atoms.calc = calc
calc.scan()

# Write to XYZ file
write('Au_bulk.xyz', atoms)

# Read from XYZ file
atoms = read('Au_bulk.xyz')

# Print atom types and positions
print("Atom types:", atoms.types)
print("Atom positions:")
for atom in atoms:
    print(atom.positions)
