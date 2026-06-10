from ase import Atoms
from ase.calculators.emt import EMT
from ase.io import write, read

# Create an Au FCC bulk
atoms = Atoms('Au', positions=[(0, 0, 0)], cell=[4.086, 4.086, 4.086], pbc=True)
atoms.calc = EMT()

# Write to an XYZ file
write('Au_fcc.xyz', atoms)

# Read the XYZ file back
atoms_read = read('Au_fcc.xyz')

# Print atom types and positions
print("Atom types:")
for atom in atoms_read:
    print(atom.symbol)

print("\nAtom positions:")
for atom in atoms_read:
    print(atom.position)
