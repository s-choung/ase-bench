from ase import Atoms
from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import crystal

# Create a bulk NaCl crystal
elements = ['Na', 'Cl']
positions = np.array([[0, 0, 0], [3.637, 0, 0], [0, 3.637, 0], [3.637, 3.637, 0],
                     [0, 0, 3.637], [3.637, 0, 3.637], [0, 3.637, 3.637], [3.637, 3.637, 3.637]])
atoms = Atoms(positions=positions, cell=[4.214, 4.214, 4.214], symbols=elements, pbc=True)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Write the crystal to a CIF file
write('NaCl.cif', atoms)

# Read the crystal back from the CIF file
atoms_read = read('NaCl.cif')

# Print the spacegroup information
print("Spacegroup:", atoms_read.get_spacegroup())

# Print the number of atoms
print("Number of atoms:", len(atoms_read))
