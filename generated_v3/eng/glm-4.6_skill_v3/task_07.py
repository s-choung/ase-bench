from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

e_initial = atoms.get_total_energy()
print(f'Initial total energy: {e_initial:.6f} eV')

md = VelocityVerlet(atoms, timestep=5*units.fs)
md.run(50)

e_final = atoms.get_total_energy()
print(f'Final total energy:   {e_final:.6f} eV')
print(f'Energy drift: {abs(e_final - e_initial):.6e} eV')
