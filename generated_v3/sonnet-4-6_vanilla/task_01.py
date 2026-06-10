from ase.build import bulk
from ase.calculators.emt import EMT

cu = bulk('Cu', 'fcc', a=3.615)
supercell = cu.repeat([2, 2, 2])

calc = EMT()
supercell.calc = calc

print("Cell vectors:")
print(supercell.cell)
print(f"\nNumber of atoms: {len(supercell)}")
print(f"\nCell lengths and angles: {supercell.cell.lengths()} {supercell.cell.angles()}")
print(f"Volume: {supercell.get_volume():.4f} Å³")
