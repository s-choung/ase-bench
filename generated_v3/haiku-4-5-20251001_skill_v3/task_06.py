from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

E_initial = atoms.get_potential_energy()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
T_initial = atoms.get_temperature()

md = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
md.run(100)

T_final = atoms.get_temperature()
E_final = atoms.get_potential_energy()

print(f"Initial Temperature: {T_initial:.2f} K")
print(f"Final Temperature: {T_final:.2f} K")
print(f"Initial Energy: {E_initial:.6f} eV")
print(f"Final Energy: {E_final:.6f} eV")
