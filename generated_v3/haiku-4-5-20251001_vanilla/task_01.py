from ase.build import bulk
from ase.build import make_supercell
import numpy as np

# Cu FCC bulk 생성
cu = bulk('Cu', 'fcc', a=3.61)

# 2x2x2 supercell 생성
P = np.array([[2, 0, 0],
              [0, 2, 0],
              [0, 0, 2]])
supercell = make_supercell(cu, P)

# Cell 정보와 원자 수 출력
print("Original cell:")
print(cu.cell)
print(f"Original atoms: {len(cu)}")
print("\nSupercell (2x2x2):")
print(supercell.cell)
print(f"Supercell atoms: {len(supercell)}")
