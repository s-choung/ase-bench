import ase.build
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Cu FCC bulk 구조 생성
initial_lattice_constant = 3.6  # 초기 격자 상수 (Angstroms)
atoms = ase.build.bulk('Cu', 'fcc', a=initial_lattice_constant)

# EMT calculator 설정
calculator = EMT()
atoms.set_calculator(calculator)

# 최적화 전 상태 출력
print("--- Initial State ---")
print(f"Initial Cell (Angstroms):\n{atoms.get_cell()}")
print(f"Initial Energy (eV): {atoms.get_potential_energy()}")
print(f"Initial Lattice Constant (Angstroms): {atoms.get_cell().lengths()[0]}")

# FrechetCellFilter 적용 (격자 상수와 원자 위치 동시 최적화)
filtered_atoms = FrechetCellFilter(atoms)

# BFGS optimizer 설정 및 실행
print("\n--- Starting Optimization ---")
optimizer = BFGS(filtered_atoms)
optimizer.run(fmax=0.01)
print("--- Optimization Finished ---")

# 최적화 후 상태 출력
print("\n--- Final State ---")
print(f"Final Cell (Angstroms):\n{atoms.get_cell()}")
print(f"Final Energy (eV): {atoms.get_potential_energy()}")
print(f"Final Lattice Constant (Angstroms): {atoms.get_cell().lengths()[0]}")
