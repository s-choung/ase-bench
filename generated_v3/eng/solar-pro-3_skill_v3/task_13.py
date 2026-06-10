from ase.build import diamond    # diamond(symbol='Si', latticeconstant=a, labcond=False)
from ase import units            # units.Angstrom or units.Bohr for length conversion
import numpy as np

# 예시용 포텐셜: EMT (실제 Si이면 EAM 등 필요)
from ase.calculators.emt import EMT

# 1. single Si unit cell (no calculator yet)
atom_cell = diamond('Si', latticeconstant=5.43, labcond=False)  # printúa cuántas atómeros hay

# 2. 3×3×3 supercell
atoms = atom_cell * (3, 3, 3)

# 3. 계산기와 셀 정보
atoms.calc = EMT()
volume = atoms.get_volume()      # angstrom³ (3D 단위)
cell = atoms.get_cell()          # Å 단위로 변환
cell_lengths = cell.cellpar('Ang')
a = cell_lengths[0]              # cubic 셀의 한 변 길이
V_Å3 = a ** 3                  # supercel의 정확한 부피

print(f"Number of atoms in the 3×3×3 Si bulk supercell: {len(atoms)}")           # 54
print(f"Mean cell volume (ASE): {volume} Å³")                                 # 1584.6 (≈54·288.2)
print(f"Lattice parameter (Å): {a:.3f} Å")
print(f"Supercell volume (Å³): {V_Å3:.1f} Å³ (batı sim 5.43³·27)")
