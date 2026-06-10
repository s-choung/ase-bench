from ase.build import bulk

# Create Cu FCC unit cell
cu_unit = bulk('Cu', 'fcc', a=3.6)

# Create 2x2x2 supercell
cu_supercell = cu_unit * (2, 2, 2)

# Print cell info
print("Cell vectors (Ångströms):")
print(cu_supercell.cell)
print(f"\nNumber of atoms: {len(cu_supercell)}")
print(f"Supercell dimensions: 2x2x2 (8 unit cells)")
