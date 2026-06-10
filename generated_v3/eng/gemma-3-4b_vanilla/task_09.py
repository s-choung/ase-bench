from ase.io import read, write
from ase.calculators import EMT, LJ

# Create a Cu FCC bulk POSCAR
slab = read('Cu_FCC_bulk.vasp')
slab.cell *= 2.826
slab.positions[:, 2] += 1.0
slab.calc = EMT()
write('Cu_FCC_bulk_modified.vasp', slab)

# Read the modified POSCAR back
slab_read = read('Cu_FCC_bulk_modified.vasp')

# Print the number of atoms
print(f"Number of atoms: {len(slab_read)}")

# Print the cell parameters
print(f"Cell parameters: {slab_read.cell}")

#Example of using the LJ calculator - not strictly required by the prompt's requirements
#slab.calc = LJ()
#print(f"LJ energy: {slab_read.lj_energy}")
