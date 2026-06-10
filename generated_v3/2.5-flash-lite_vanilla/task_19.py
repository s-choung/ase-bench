from ase import Atoms
from ase.calculators.emt import EMT
from ase.neighborlist import natural_cutoffs, NeighborList

# CO2 분자 생성
atoms = Atoms('CO2',
              positions=[(0, 0, 0), (-1.16, 0, 0), (1.16, 0, 0)],
              cell=[10, 10, 10],
              pbc=False)

# EMT 계산기 할당 (필수는 아니지만 예시로 포함)
atoms.calc = EMT()

# 원자 간 거리 계산
distances = atoms.get_distances(0, [1, 2])
print(f"Distance between C(0) and O(1): {distances[0]:.2f} Angstrom")
print(f"Distance between C(0) and O(2): {distances[1]:.2f} Angstrom")

# 모든 원자 쌍 간 거리 계산 (선택 사항)
all_distances = atoms.get_all_distances()
print("\nAll pairwise distances:")
for i in range(len(atoms)):
    for j in range(i + 1, len(atoms)):
        print(f"Distance between atom {i} and atom {j}: {all_distances[i, j]:.2f} Angstrom")
