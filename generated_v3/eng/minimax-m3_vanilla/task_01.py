from ase.build import bulk

atoms = bulk('Cu', crystalstructure='fcc', a=3.6)
print("Primitive FCC Cu unit cell")
print(f"Number of atoms: {len(atoms)}")
print(f"Cell parameters (Angstrom): {atoms.cell.cellpar()}")
print(f"Volume: {atoms.get_volume():.3f} Angstrom^3\n")

supercell = atoms.repeat((2, 2, 2))
print("2x2x2 supercell")
print(f"Number of atoms: {len(supercell)}")
print(f"Cell parameters (Angstrom): {supercell.cell.cellpar()}")
print(f"Volume: {supercell.get_volume():.3f} Angstrom^3")
