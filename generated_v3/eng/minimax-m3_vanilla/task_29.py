from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet

atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)

e0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn.run(200)
e1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {e0:.6f} eV")
print(f"Final total energy:   {e1:.6f} eV")
print(f"Energy difference:    {e1 - e0:.6f} eV")
