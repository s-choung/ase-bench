from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89, cubic=True)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=2.0 * units.fs)

e_start = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn.run(200)
e_end = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Total energy difference: {e_end - e_start:.6f} eV")
