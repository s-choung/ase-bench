from ase import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs

atoms = bulk('Cu', 'fcc').repeat((2,2,2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

T0 = atoms.get_temperature()
E0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial T: {T0:.2f} K, Total E: {E0:.3f} eV")

dyn = Langevin(atoms, timestep=5*fs, temperature_K=300, friction=0.01)

for _ in range(100):
    dyn.step()

Tf = atoms.get_temperature()
Ef = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final T: {Tf:.2f} K, Total E: {Ef:.3f} eV")
