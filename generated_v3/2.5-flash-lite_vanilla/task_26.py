from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase import units

# Ni FCC bulk 생성 (2x2x2 supercell)
atoms = fcc111('Ni', size=(2, 2, 2), vacuum=10.0)

# EMT calculator 설정
atoms.calc = EMT(rcut=10.0)

# PreconLBFGS optimizer 설정
optimizer = PreconLBFGS(atoms, precon='auto')

# 구조 최적화 실행
optimizer.run(fmax=0.01)

# 결과 출력
print(f"Number of steps: {optimizer.get_number_of_steps()}")
print(f"Final energy: {atoms.get_total_energy() / units.eV:.4f} eV")
print(f"Cell parameters: {atoms.get_cell().lengths()}")
