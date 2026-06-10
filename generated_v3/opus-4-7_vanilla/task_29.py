from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89, cubic=True).repeat((2,2,2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = VelocityVerlet(atoms, timestep=2.0*units.fs)

E0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn.run(200)
E1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {E0:.6f} eV")
print(f"Final total energy:   {E1:.6f} eV")
print(f"Energy difference:    {E1-E0:.6e} eV")
