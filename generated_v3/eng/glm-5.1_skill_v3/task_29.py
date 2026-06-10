from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Pd', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

e_start = atoms.get_potential_energy() + atoms.get_kinetic_energy()

md = VelocityVerlet(atoms, 2 * units.fs)
md.run(200)

e_end = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Total energy difference (end - start): {e_end - e_start:.6e} eV")
