from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase import units

# Cu FCC bulk 생성
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# 최적화 전 정보 출력
print(f"Before optimization:")
print(f"  Cell: {atoms.get_cell().lengths()}")
print(f"  Energy: {atoms.get_potential_energy():.4f} eV")

# FrechetCellFilter와 BFGS optimizer를 사용한 최적화
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# 최적화 후 정보 출력
print(f"\nAfter optimization:")
print(f"  Cell: {atoms.get_cell().lengths()}")
print(f"  Energy: {atoms.get_potential_energy():.4f} eV")
