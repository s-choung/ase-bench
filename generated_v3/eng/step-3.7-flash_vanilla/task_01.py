from ase.build import bulk

cu = bulk('Cu', 'fcc', supercell=(2, 2, 2))
print("Cell lengths (Å):", cu.cell.lengths())
print("Cell angles (deg):", cu.cell.angles())
print("Number of atoms:", len(cu))
