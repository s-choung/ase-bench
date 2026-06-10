from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

e_init = atoms.get_total_energy()
print(f"Initial total energy: {e_init:.6f} eV")

dyn = VelocityVerlet(atoms, timestep=5 * units.fs)
dyn.run(50)

e_final = atoms.get_total_energy()
print(f"Final total energy: {e_final:.6f} eV")
