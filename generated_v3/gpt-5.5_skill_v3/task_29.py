from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Pd", "fcc", a=3.89, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

e0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

e1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {e0:.8f} eV")
print(f"Final total energy:   {e1:.8f} eV")
print(f"Energy difference:    {e1 - e0:.8e} eV")
