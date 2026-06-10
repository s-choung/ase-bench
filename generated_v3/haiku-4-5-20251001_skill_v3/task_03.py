from ase.build import mx2, add_vacuum
from ase import Atoms

atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=0)
add_vacuum(atoms, 10.0)

cell = atoms.get_cell()
print("Cell parameters:")
print(f"a = {cell[0, 0]:.4f} Å")
print(f"b = {cell[1, 1]:.4f} Å")
print(f"c = {cell[2, 2]:.4f} Å")
print(f"\nFull cell:\n{cell}")
print(f"\nNumber of atoms: {len(atoms)}")
