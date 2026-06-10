from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
dyn.run(100)
print(f"Initial Energy: {atoms.get_potential_energy()} eV")
print(f"Initial Temperature: {atoms.get_temperature()} K")
print(f"Final Energy: {atoms.get_potential_energy()} eV")
print(f"Final Temperature: {atoms.get_temperature()} K")
