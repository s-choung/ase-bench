from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.io import read, write

# Pt(111) 3층 slab 생성
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# CO 분자 생성 및 slab에 흡착 (예시 위치)
from ase.build import molecule
co = molecule('CO')
co.translate([1.0, 1.0, 3.0])
slab.extend(co)

# Calculator 설정
slab.calc = EMT()

# 하부 1층 고정
constraint_fix_atoms = FixAtoms(indices=[atom.index for atom in slab if atom.tag == 0])
slab.set_constraint(constraint_fix_atoms)

# CO C-O 결합 고정
# CO 분자의 인덱스를 찾아야 함. slab에 추가된 순서에 따라 달라질 수 있음.
# 여기서는 slab에 추가된 마지막 두 원자가 CO라고 가정.
co_indices = [len(slab) - 2, len(slab) - 1]
constraint_fix_bond = FixBondLength(co_indices[0], co_indices[1])
slab.constraints.append(constraint_fix_bond)

# BFGS 최적화
optimizer = BFGS(slab, trajectory='opt.traj', logfile='opt.log')
optimizer.run(fmax=0.05)

# 최종 에너지 출력
final_energy = slab.get_potential_energy()
print(f"Final Energy: {final_energy:.4f} eV")

# 최종 C-O 거리 출력
co_distance = slab.get_distance(co_indices[0], co_indices[1])
print(f"C-O Distance: {co_distance:.4f} Angstrom")
