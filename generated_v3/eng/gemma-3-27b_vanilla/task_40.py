from ase.build import fcc111
from ase.io import write, read
from ase.lattice.cubic import FaceCenteredCubic

atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                           symbol='NaCl',
                           latticeconstant=5.64,
                           pbc=(True, True, True))

write('NaCl.cif', atoms)
atoms_read = read('NaCl.cif')

print(f"Spacegroup: {atoms_read.get_spacegroup_symbol()}")
print(f"Number of atoms: {len(atoms_read)}")
