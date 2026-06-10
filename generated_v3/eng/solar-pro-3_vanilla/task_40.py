import ase.io
import ase.atom
from ase import Atoms

# Create a 2x2x2 NaCl supercell
a = 5.64  # NaCl lattice constant in Å
NaCl = Atoms('NaCl2', cell=(a, a, a), pbc=True)
NaCl.add_ghost('NaCl2')  # extend basis to fill the cell
NaCl.set_cell((a*2, a*2, a*2), scale_atoms=True)

# Write as CIF
ase.io.write('NaCl_supercell.cif', NaCl)

# Read back
loaded = ase.io.read('NaCl_supercell.cif')
print(f"Spacegroup: {loaded.get_spacegroup()}")
print(f"Spacegroup number: {loaded.get_spacegroup_number()}")
print(f"Number of atoms: {len(loaded)}")
