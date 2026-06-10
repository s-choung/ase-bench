from ase.spacegroup import crystal
from ase.io import write, read

# 1. NaCl 결정 구조 생성
# NaCl은 Fm-3m (spacegroup 225) 구조를 가지며, Na를 (0,0,0)에 두면 Cl은 (0.5,0.5,0.5)에 자동으로 배치됩니다.
# 격자 상수 a=5.64 Å 사용.
nacl_atoms = crystal(
    symbols='NaCl',
    basis=[(0, 0, 0)],
    spacegroup=225,
    cellpar=5.64
)

# 2. CIF 형식으로 저장
write('nacl.cif', nacl_atoms)

# 3. CIF 파일에서 다시 읽어오기
read_atoms = read('nacl.cif')

# 4. Spacegroup 정보 출력
spacegroup_info = read_atoms.get_spacegroup()
print(f"Spacegroup number: {spacegroup_info.no}")
print(f"Spacegroup symbol: {spacegroup_info.symbol}")

# 5. 원자 수 출력
print(f"Number of atoms: {len(read_atoms)}")
