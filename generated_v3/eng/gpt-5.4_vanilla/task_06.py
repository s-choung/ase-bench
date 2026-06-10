from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T = 300.0
dt_fs = 5.0
steps = 100
friction = 0.01 / units.fs

MaxwellBoltzmannDistribution(atoms, temperature_K=T)
Stationary(atoms)

def temperature(a):
    return a.get_kinetic_energy() / (1.5 * len(a) * units.kB)

e0 = atoms.get_total_energy()
t0 = temperature(atoms)

dyn = Langevin(atoms, timestep=dt_fs * units.fs, temperature_K=T, friction=friction)
dyn.run(steps)

e1 = atoms.get_total_energy()
t1 = temperature(atoms)

print(f"Initial temperature: {t0:.2f} K")
print(f"Initial total energy: {e0:.6f} eV")
print(f"Final temperature: {t1:.2f} K")
print(f"Final total energy: {e1:.6f} eV")
