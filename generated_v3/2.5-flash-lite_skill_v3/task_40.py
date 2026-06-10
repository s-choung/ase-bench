from ase.io import read, write
from ase.spacegroup import crystal

# NaCl 결정 구조 생성
# NaCl은 FCC 격자 기반이며, 공간군 225 (Fm-3m)를 가집니다.
# 각 원소의 상대적 위치를 지정합니다.
# Na는 (0,0,0)에, Cl은 (0.5, 0.5, 0.5)에 위치합니다.
# 격자 상수 a는 약 5.64 Å 입니다.
atoms = crystal(
    'NaCl',
    [(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90],
    primitive=False,  # Fm-3m은 비원시 셀입니다.
    pbc=True
)

# CIF 형식으로 저장
write('nacl.cif', atoms, format='cif')

# CIF 파일 읽어오기
atoms_read = read('nacl.cif', format='cif')

# Spacegroup 정보 출력
print(f"Spacegroup: {atoms_read.info['spacegroup']}")

# 원자 수 출력
print(f"Number of atoms: {len(atoms_read)}")
