import ase.build
import ase.io

atoms = ase.build.bulk('Au', 'fcc', a=4.08)
ase.io.write('Au_fcc.xyz', atoms)
atoms_read = ase.io.read('Au_fcc.xyz')
print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions:\n", atoms_read.positions)
