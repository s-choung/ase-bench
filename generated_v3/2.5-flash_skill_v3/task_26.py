from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter
from ase import units

# 1. Ni FCC bulk 구조 생성
# Ni의 격자 상수는 대략 3.52 Å (EMT는 Cu, Ag, Au, Ni, Pd, Pt, Al에 적합)
atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. FrechetCellFilter를 사용하여 셀과 원자 위치를 동시에 최적화
# PreconLBFGS는 필터 객체를 직접 받음
filtered_atoms = FrechetCellFilter(atoms)

# 4. PreconLBFGS optimizer 설정 및 실행
# precon='auto'는 PreconLBFGS의 기본 동작
optimizer = PreconLBFGS(filtered_atoms, trajectory='ni_bulk_opt.traj')
optimizer.run(fmax=0.01)

# 5. 결과 출력
print(f"Optimization finished in {optimizer.get_number_of_steps()} steps.")
print(f"Final potential energy: {atoms.get_potential_energy():.4f} eV")
cell_lengths_angles = atoms.get_cell_lengths_and_angles()
print(f"Final cell parameters (a, b, c): {cell_lengths_angles[0]:.4f}, {cell_lengths_angles[1]:.4f}, {cell_lengths_angles[2]:.4f} Å")
print(f"Final cell angles (alpha, beta, gamma): {cell_lengths_angles[3]:.2f}, {cell_lengths_angles[4]:.2f}, {cell_lengths_angles[5]:.2f} degrees")
