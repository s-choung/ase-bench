from ase import Atoms
from ase.build import bulk
from ase.io import read, write
from ase.calculators.emt import EMT

# Create a Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms)
opt.run(fmax=0.05, steps=1000)

# Write the optimized structure to a VASP POSCAR file
write('cu_fcc.poscar', atoms, format='vasp')

# Read the structure back from the VASP POSCAR file
atoms_read = read('cu_fcc.poscar', format='vasp')

# Print the number of atoms
print(f"Number of atoms: {len(atoms_read)}")

# Print the cell parameters
cell = atoms_read.get_cell()
print(f"Cell parameters: {cell}")
