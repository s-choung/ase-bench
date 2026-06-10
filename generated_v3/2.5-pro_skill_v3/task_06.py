import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# 1. 구조 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# 2. MD 초기화
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# 3. 초기 상태 출력
print("Initial State:")
print(f"  Temperature: {atoms.get_temperature():.2f} K")
print(f"  Potential Energy: {atoms.get_potential_energy():.4f} eV")
print(f"  Kinetic Energy: {atoms.get_kinetic_energy():.4f} eV")
print(f"  Total Energy: {atoms.get_total_energy():.4f} eV")
print("-" * 20)

# 4. Langevin MD 실행
dyn = Langevin(atoms,
               timestep=5 * units.fs,
               temperature_K=300,
               friction=0.01 / units.fs,
               trajectory='cu_md.traj',
               logfile='cu_md.log')

dyn.run(100)

# 5. 최종 상태 출력
print("Final State:")
print(f"  Temperature: {atoms.get_temperature():.2f} K")
print(f"  Potential Energy: {atoms.get_potential_energy():.4f} eV")
print(f"  Kinetic Energy: {atoms.get_kinetic_energy():.4f} eV")
print(f"  Total Energy: {atoms.get_total_energy():.4f} eV")
