from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Cu FCC bulk 생성
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# 최적화 전 정보
cell_before = atoms.get_cell_lengths_and_angles()
energy_before = atoms.get_potential_energy()
print(f"Before optimization:")
print(f"  Cell: a={cell_before[0]:.6f} Å, b={cell_before[1]:.6f} Å, c={cell_before[2]:.6f} Å")
print(f"  Energy: {energy_before:.6f} eV")

# FrechetCellFilter를 사용한 셀+위치 동시 최적화
opt = BFGS(FrechetCellFilter(atoms), trajectory='opt.traj')
opt.run(fmax=0.01)

# 최적화 후 정보
cell_after = atoms.get_cell_lengths_and_angles()
energy_after = atoms.get_potential_energy()
print(f"\nAfter optimization:")
print(f"  Cell: a={cell_after[0]:.6f} Å, b={cell_after[1]:.6f} Å, c={cell_after[2]:.6f} Å")
print(f"  Energy: {energy_after:.6f} eV")
print(f"\nEnergy change: {energy_after - energy_before:.6f} eV")
