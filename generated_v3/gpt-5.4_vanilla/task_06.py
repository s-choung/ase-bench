from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def temperature(a):
    return 2.0 * a.get_kinetic_energy() / (3.0 * len(a) * units.kB)

e0 = atoms.get_total_energy()
t0 = temperature(atoms)

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01)
dyn.run(100)

e1 = atoms.get_total_energy()
t1 = temperature(atoms)

print(f"Initial temperature: {t0:.2f} K")
print(f"Initial total energy: {e0:.6f} eV")
print(f"Final temperature: {t1:.2f} K")
print(f"Final total energy: {e1:.6f} eV")
