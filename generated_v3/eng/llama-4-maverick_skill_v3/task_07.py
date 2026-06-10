from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

initial_energy = atoms.get_total_energy()
print(f'Initial total energy: {initial_energy:.4f} eV')

dyn = VelocityVerlet(atoms, timestep=5*units.fs)
dyn.run(50)

final_energy = atoms.get_total_energy()
print(f'Final total energy: {final_energy:.4f} eV')
print(f'Energy conservation check: {abs(final_energy - initial_energy):.6f} eV')
