from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
e_initial = atoms.get_total_energy()
dyn = VelocityVerlet(atoms, timestep=5*units.fs)
dyn.run(50)
e_final = atoms.get_total_energy()
print(f"Initial energy: {e_initial:.6f} eV")
print(f"Final energy: {e_final:.6f} eV")
