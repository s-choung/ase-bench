from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

E0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

dyn = VelocityVerlet(atoms, timestep=2*units.fs)
dyn.run(200)

E1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {E0:.6f} eV")
print(f"Final   total energy: {E1:.6f} eV")
print(f"Difference (E1-E0):   {E1-E0:.6e} eV")
print(f"Final temperature:    {atoms.get_temperature():.2f} K")
