from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300)
Stationary(atoms)

T_initial = atoms.get_temperature()
E_initial = atoms.get_potential_energy()
dyn = Langevin(atoms, 5*units.fs, 300, 0.01/units.fs)
dyn.run(100)
T_final = atoms.get_temperature()
E_final = atoms.get_potential_energy()

print(f"Initial: T={T_initial:.2f} K, E={E_initial:.6f} eV")
print(f"Final: T={T_final:.2f} K, E={E_final:.6f} eV")
