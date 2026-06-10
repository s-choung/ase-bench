from ase.build import bulk
from ase.io import write, read
import os

# 1. Au FCC bulk 구조 생성
atoms = bulk('Au', 'fcc', a=4.08, cubic=True)

# 2. XYZ 형식 파일로 저장
filename = 'au_fcc_bulk.xyz'
write(filename, atoms)
print(f"'{filename}' 파일에 Au FCC bulk 구조를 저장했습니다.")

# 3. XYZ 파일 다시 읽기
read_atoms = read(filename)
print(f"'{filename}' 파일에서 구조를 읽었습니다.")

# 4. 원자 종류와 위치 print
print("\n읽어온 원자 정보:")
for i, atom in enumerate(read_atoms):
    print(f"Atom {i+1}: Symbol={atom.symbol}, Position={atom.position}")

# 생성된 파일 삭제 (선택 사항)
os.remove(filename)
print(f"\n'{filename}' 파일을 삭제했습니다.")
