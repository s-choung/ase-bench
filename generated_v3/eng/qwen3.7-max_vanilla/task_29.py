from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Pd', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)

E_start = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn.run(200)
E_end = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Total energy difference (End - Start): {E_end - E_start:.6f} eV")
