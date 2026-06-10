from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)

e_start = atoms.get_total_energy()
dyn.run(200)
e_end = atoms.get_total_energy()

print(f"Total energy difference: {e_end - e_start:.8f} eV")
