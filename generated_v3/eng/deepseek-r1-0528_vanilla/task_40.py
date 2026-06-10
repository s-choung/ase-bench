from ase.build import bulk
import ase.io

structure = bulk('NaCl', crystalstructure='rocksalt', a=5.64)
ase.io.write('nacl.cif', structure)
read_structure = ase.io.read('nacl.cif')

spacegroup_symbol = read_structure.info.get('spacegroup', 'Unknown')
print(f"Spacegroup: {spacegroup_symbol}")
print(f"Number of atoms: {len(read_structure)}")
