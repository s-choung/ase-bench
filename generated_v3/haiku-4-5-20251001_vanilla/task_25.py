from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

# Cu FCC bulk 구조 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# 최적화 전 정보
print("=== Before Optimization ===")
print(f"Cell volume: {atoms.get_volume():.4f} Ų")
print(f"Cell parameters: {atoms.cell.cellpar()[:3]}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")

# FrechetCellFilter를 사용하여 cell과 atomic positions 동시 최적화
ucf = FrechetCellFilter(atoms)
optimizer = BFGS(ucf, trajectory='optimization.traj')
optimizer.run(fmax=0.01)

# 최적화 후 정보
print("\n=== After Optimization ===")
print(f"Cell volume: {atoms.get_volume():.4f} Ų")
print(f"Cell parameters: {atoms.cell.cellpar()[:3]}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
print(f"Lattice constant a: {atoms.cell.cellpar()[0]:.6f} Ų")
