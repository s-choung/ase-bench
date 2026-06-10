from ase.build import bulk
from ase.spacegroup import crystal

a = 2.95
c_a_ratio = 1.59
c = a * c_a_ratio

# ASE의 bulk 함수는 c/a 비율을 직접 설정하는 옵션이 없으므로,
# crystal 함수를 사용하여 HCP 구조를 명시적으로 생성합니다.
# HCP의 공간군은 194번 (P6_3/mmc) 입니다.
# Ti의 원자 번호는 22번입니다.
atoms = crystal(symbol='Ti',
                basis={'Ti': [(0, 0, 0), (1/3, 2/3, 1/2)]},
                spacegroup=194,
                cell=[a, a, c, 90, 90, 120],
                primitive=False)

print("Cell vectors:")
print(atoms.get_cell())
print("\nAtom positions:")
print(atoms.get_positions())
