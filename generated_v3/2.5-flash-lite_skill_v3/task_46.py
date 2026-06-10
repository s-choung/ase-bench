from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import read, write

# 1. Slab 생성
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# 2. CO 분자 생성 및 흡착
co = molecule('CO')
# CO의 C 원자 인덱스를 찾습니다. (일반적으로 0번)
c_index = co.symbols.index('C')
# Slab에 CO 흡착 (ontop 위치, 높이 1.8 Å)
# add_adsorbate는 slab 객체를 직접 수정합니다.
from ase.build import add_adsorbate
add_adsorbate(slab, co, height=1.8, position='ontop')

# 3. Constraint 설정
# 하부 1층 고정 (z 좌표 기준)
# slab의 z 좌표를 기준으로 하부 1층을 결정합니다.
z_coords = slab.get_positions()[:, 2]
min_z = min(z_coords)
# tolerance를 사용하여 z 좌표가 거의 같은 원자들을 선택합니다.
tolerance = 0.1
fixed_indices = [atom.index for atom in slab if abs(atom.position[2] - min_z) < tolerance]
constraint_fix_atoms = FixAtoms(indices=fixed_indices)

# CO의 C-O 결합 고정
# 흡착된 CO 분자의 C와 O 원자 인덱스를 찾습니다.
# add_adsorbate 후 CO 원자들은 slab의 마지막 원자들이 됩니다.
co_atoms_indices = [atom.index for atom in slab if atom.symbol == 'C' or atom.symbol == 'O']
c_atom_index_in_slab = [i for i in co_atoms_indices if slab[i].symbol == 'C'][0]
o_atom_index_in_slab = [i for i in co_atoms_indices if slab[i].symbol == 'O'][0]
constraint_fix_bond = FixBondLength(c_atom_index_in_slab, o_atom_index_in_slab)

# 두 constraint를 slab에 적용
slab.set_constraint([constraint_fix_atoms, constraint_fix_bond])

# 4. Calculator 설정
slab.calc = EMT()

# 5. 최적화
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# 6. 결과 출력
final_energy = slab.get_potential_energy()
# C-O 결합 길이를 다시 계산합니다.
co_atoms_indices_final = [atom.index for atom in slab if atom.symbol == 'C' or atom.symbol == 'O']
c_atom_index_final = [i for i in co_atoms_indices_final if slab[i].symbol == 'C'][0]
o_atom_index_final = [i for i in co_atoms_indices_final if slab[i].symbol == 'O'][0]
co_distance = slab.get_distance(c_atom_index_final, o_atom_index_final)

print(f"Final Energy: {final_energy:.4f} eV")
print(f"C-O bond length: {co_distance:.4f} Å")
