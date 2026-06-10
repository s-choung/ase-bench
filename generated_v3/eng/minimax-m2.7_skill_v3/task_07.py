from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = Atoms('Cu', cell=[[2.2, 0, 0], [0, 2.2, 0], [0, 0, 2.2]], pbc=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

e_initial = atoms.get_total_energy()

VelocityVerlet(atoms, timestep=5 * units.fs).run(steps=50)

e_final = atoms.get_total_energy()

print(f"Initial total energy: {e_initial:.6f} eV")
print(f"Final total energy:   {e_final:.6f} eV")
print(f"Energy drift:         {e_final - e_initial:.6f} eV")
