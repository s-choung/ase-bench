from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# Create NaCl rock‑salt structure
atoms = bulk('NaCl', 'rocksalt', a=5.64)

# Save to CIF and read back
write('NaCl.cif', atoms)
atoms_back = read('NaCl.cif')

# Space‑group info and atom count
sg = get_spacegroup(atoms_back)
print(f"Spacegroup: {sg.symbol} ({sg.no})")
print(f"Number of atoms: {len(atoms_back)}")
