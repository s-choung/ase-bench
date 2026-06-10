from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

E0 = atoms.get_kinetic_energy() + atoms.get_potential_energy()

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

E1 = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"dE = {E1 - E0:.6e} eV")
