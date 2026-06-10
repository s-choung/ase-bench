from ase.build import bulk
from ase.io import write, read

# Au FCC bulk 생성
atoms = bulk('Au', 'fcc', a=4.0)

# XYZ 형식으로 파일 저장
write('au_fcc.xyz', atoms)

# 파일에서 다시 읽기
atoms_read = read('au_fcc.xyz')

# 원자 종류와 위치 출력
for atom in atoms_read:
    print(f"Element: {atom.symbol}, Position: {atom.position}")
