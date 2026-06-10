from ase import Atoms
from ase.build import add_ideal_gas_temperature
from ase.io import write, read
from ase.spacegroup import Spacegroup

atoms = Atoms('NaCl',
              positions=[(0, 0, 0), (0.5, 0.5, 0)],
              cell=[3.5, 3.5, 3.5, 90, 90, 90])
atoms.set_pbc(True)

write('NaCl.cif', atoms, format='cif')

atoms_read = read('NaCl.cif', format='cif')

sg = Spacegroup.from_cell(atoms_read.cell, positions=atoms_read.positions, symbols = [atom.symbol for atom in atoms_read])
spacegroup_number = sg.number

print(f"Spacegroup: {spacegroup_number}")
print(f"Number of atoms: {len(atoms_read)}")
