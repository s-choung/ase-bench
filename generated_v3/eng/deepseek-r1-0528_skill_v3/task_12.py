from ase.build import bulk

atoms = bulk('Ti', 'hcp', a=2.95, covera=1.59)
print("Cell vectors (Å):")
print(atoms.cell.get_cell_lengths_and_angles()[:3])
print(f"\nAtomic positions (Å):")
for i, pos in enumerate(atoms.positions):
    print(f"Ti{i+1}: {pos.round(6)}")
