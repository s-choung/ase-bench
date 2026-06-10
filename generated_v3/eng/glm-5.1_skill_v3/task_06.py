from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

E_init = atoms.get_potential_energy()
T_init = atoms.get_temperature()

md = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
md.run(steps=100)

E_final = atoms.get_potential_energy()
T_final = atoms.get_temperature()

print(f"Initial: T = {T_init:.2f} K, E = {E_init:.4f} eV")
print(f"Final:   T = {T_final:.2f} K, E = {E_final:.4f} eV")
