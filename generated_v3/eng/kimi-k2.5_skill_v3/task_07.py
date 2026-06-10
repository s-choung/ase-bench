from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f"Initial total energy: {atoms.get_total_energy():.6f} eV")
dyn = VelocityVerlet(atoms, timestep=5*units.fs)
dyn.run(50)
print(f"Final total energy: {atoms.get_total_energy():.6f} eV")
