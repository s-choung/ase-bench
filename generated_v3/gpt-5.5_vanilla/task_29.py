from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet

atoms = bulk("Pd", "fcc", a=3.89, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500, force_temp=True)

e0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

dyn = VelocityVerlet(atoms, timestep=2.0 * units.fs)
dyn.run(200)

e1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {e0:.12f} eV")
print(f"Final total energy:   {e1:.12f} eV")
print(f"Energy difference:    {e1 - e0:.12e} eV")
