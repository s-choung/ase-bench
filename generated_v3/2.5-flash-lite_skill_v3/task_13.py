from ase.build import bulk
from ase.build import make_supercell
import numpy as np

# Diamond 구조의 Si bulk 생성
atoms = bulk('Si', 'diamond', a=5.43)

# 3x3x3 supercell 생성
P = np.diag([3, 3, 3])
supercell_atoms = make_supercell(atoms, P)

# 원자 수와 cell volume 출력
num_atoms = len(supercell_atoms)
cell_volume = supercell_atoms.get_volume()

print(f"Number of atoms in the supercell: {num_atoms}")
print(f"Cell volume of the supercell: {cell_volume:.2f} Å³")
