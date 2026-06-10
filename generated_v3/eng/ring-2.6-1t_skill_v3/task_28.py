from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

T0, T1 = 300, 600
nsteps = 200
dt = 5 * units.fs

dyn = Langevin(atoms, timestep=dt, temperature_K=T0, friction=0.01 / units.fs)
MaxwellBoltzmannDistribution(atoms, temperature_K=T0)
Stationary(atoms)

for step in range(nsteps):
    T = T0 + (T1 - T0) * step / (nsteps - 1)
    dyn.temperature = T
    dyn.run(1)
    if (step + 1) % 50 == 0:
        print(f'Step {step + 1}: T = {atoms.get_temperature():.1f} K')
