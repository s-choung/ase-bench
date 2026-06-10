from ase import Atoms
from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89, cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = VelocityVerlet(atoms, timestep=2.0 * units.fs)
E0 = atoms.get_total_energy()
dyn.run(200)
E1 = atoms.get_total_energy()

print(f"Energy difference: {E1 - E0:.6f} eV")
