from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as u

atoms = Atoms('Cu', positions=[(0, 0, 0), (0, 0, 3.6), (3.6, 0, 0), (3.6, 3.6, 0),
                                (0, 3.6, 3.6), (3.6, 3.6, 3.6)],
              cell=[[3.6, 0, 0], [0, 3.6, 0], [0, 0, 3.6]])
atoms.set_cell([[3.6, 0, 0], [0, 3.6, 0], [0, 0, 3.6]], scale_atoms=True)
atoms.repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5 * u.fs, temperature_K=300, friction=0.01 / u.fs)
dyn.run(100)

print(f"Initial Temperature: {atoms.get_temperature():.2f} K")
print(f"Final Temperature: {atoms.get_temperature():.2f} K")
print(f"Initial Energy: {atoms.get_potential_energy():.2f} eV")
print(f"Final Energy: {atoms.get_potential_energy():.2f} eV")
