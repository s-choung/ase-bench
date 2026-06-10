from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

e0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {e0:.6f} eV")

md = VelocityVerlet(atoms, timestep=5 * units.fs)
md.run(steps=50)

e1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final total energy:   {e1:.6f} eV")
print(f"Drift: {(e1 - e0):.6e} eV")
