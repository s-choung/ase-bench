from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase import Atoms
import numpy as np

# Cu FCC 2x2x2 supercell 생성
atoms = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)
atoms.calc = EMT()

# 0번 원자와 나머지 모든 원자 사이의 거리 계산
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)

# 최소 거리와 최대 거리 출력
min_distance = np.min(distances)
max_distance = np.max(distances)

print(f"Minimum distance: {min_distance:.4f} Å")
print(f"Maximum distance: {max_distance:.4f} Å")
