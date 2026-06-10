from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet
from ase import units

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

e0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

e1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {e0:.6f} eV")
print(f"Final total energy:   {e1:.6f} eV")
