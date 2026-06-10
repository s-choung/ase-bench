from ase import bulk, read, write

atoms = bulk('NaCl', 'rocksalt', a=5.64)
write('nacl.cif', atoms)
loaded = read('nacl.cif')
print(f"Space group: {loaded.info['spacegroup']} (No. {loaded.info['spacegroup_number']})")
print(f"Number of atoms: {len(loaded)}")
