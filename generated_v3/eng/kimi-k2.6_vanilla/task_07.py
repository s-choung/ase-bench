from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = VelocityVerlet(atoms, 5 * units.fs)
print(f"Initial: {atoms.get_total_energy():.6f} eV")
dyn.run(50)
print(f"Final:   {atoms.get_total_energy():.6f} eV")
