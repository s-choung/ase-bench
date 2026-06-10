from ase.build import fcc111, add_vacuum
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
import numpy as np

# Al(111) slab 생성 (3층)
slab = fcc111('Al', size=(4, 4, 3), a=4.05, vacuum=10.0)

# N2 분자 생성
n2 = molecule('N2')
n2.center()

# N2를 bridge 사이트에 배치
# Al(111)의 bridge 사이트 찾기
slab_center = slab.get_center_of_mass()
bridge_x = slab.positions[0, 0] + 1.43  # Al lattice constant/2 근처
bridge_y = slab.positions[0, 1] + 1.43
bridge_z = slab.positions[:, 2].max() + 2.0  # height 2.0 Å

# N2 분자 위치 설정
n2_center = np.array([bridge_x, bridge_y, bridge_z])
n2.translate(n2_center - n2.get_center_of_mass())

# slab과 n2 결합
from ase import Atoms
structure = Atoms(slab.get_chemical_symbols() + n2.get_chemical_symbols(),
                  positions=np.vstack([slab.positions, n2.positions]),
                  cell=slab.cell,
                  pbc=slab.pbc)

# 하단 2층 고정
z_positions = structure.positions[:, 2]
z_unique = np.unique(z_positions)
z_unique.sort()
fixed_z_threshold = z_unique[1]
constraint = FixAtoms(mask=z_positions < fixed_z_threshold)
structure.set_constraint(constraint)

# 결과 출력
print(f"Total number of atoms: {len(structure)}")
print(f"Atomic species: {set(structure.get_chemical_symbols())}")
print(f"Composition: Al={structure.get_chemical_symbols().count('Al')}, N={structure.get_chemical_symbols().count('N')}")
