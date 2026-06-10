from ase import Atoms
from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import crystal_info

# NaCl를 fcc( rock‑salt ) 구조로 생성
atoms = bulk('NaCl', 'rocksalt')          # automatically periodic, cell optimized

# CIF 파일 저장
write('NaCl.cif', atoms, format='cif')

# 읽기
atoms_r = read('NaCl.cif', format='cif')

# 공간군 정보 추출
sgrp_info = crystal_info(atoms_r)
print('Spacegroup:', sgrp_info)
print('Number of atoms:', len(atoms_r))
