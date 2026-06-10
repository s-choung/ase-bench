from ase import Atoms
from ase.lattice import crystal

# Create NaCl crystal structure (rock-salt structure)
atoms = crystal(['Na', 'Cl'], 
                basis=[(0, 0, 0), (0.5, 0.5, 0.5)], 
                cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Save to CIF format
atoms.write('NaCl.cif')

# Read the CIF file back
atoms_read = Atoms(read='NaCl.cif')

# Print spacegroup information
print("Spacegroup:", atoms_read.get_spacegroup())

# Print number of atoms
print("Number of atoms:", len(atoms_read))
