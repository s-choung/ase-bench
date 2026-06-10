from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2,2,2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

T_init = atoms.get_temperature()
E_init = atoms.get_total_energy()
print(f"Initial T: {T_init:.2f} K, E: {E_init:.4f} eV")

dyn = Langevin(atoms, 5*units.fs, temperature_K=300, friction=0.01)
dyn.run(100)

T_final = atoms.get_temperature()
E_final = atoms.get_total_energy()
print(f"Final   T: {T_final:.2f} K, E: {E_final:.4f} eV")
