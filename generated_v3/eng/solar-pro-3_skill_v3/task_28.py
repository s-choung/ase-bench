from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixLaplacian
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import thermostat

# 1. Build Cu FCC supercell (2x2x2)
atoms = bulk('Cu', 'fcc', a='3.5', cubic=True) * (2, 2, 2)

# 2. Initial geometry minimization
calc = EMT()
atoms.calc = calc
BFGS(atoms, trajectory='relax.traj').run(fmax=0.02)

# 3. Langevin MD setup
thermo = thermostat.Langevin(atoms,
                             timestep=5 * units.fs,
                             temperature_K=300,
                             friction=0.01 / units.fs)

# 4. Temperature ramp (300K → 600K) over 200 steps
thermo.temperature = 300.0
for step in range(200):
    thermo.run(1)
    if step % 50 == 0:
        print(f'Step {step}, T = {thermo.get_temperature():.2f} K')

    if step == 199:                     # 마지막 스텝에서 목표 온도 설정
        thermo.set_temperature(600.0)
