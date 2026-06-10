from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk("Pd", "fcc", cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

e0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

e1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Energy difference after 200 steps: {e1 - e0:.8e} eV")
