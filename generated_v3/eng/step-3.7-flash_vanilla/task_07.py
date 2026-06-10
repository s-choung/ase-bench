import numpy as np
from ase import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.md import VelocityVerlet
import ase.units as units

atoms = bulk('Cu', 'fcc', a=3.615)
atoms.calc = EMT()
np.random.seed(0)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
e_initial = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn = VelocityVerlet(atoms, dt=1.0 * units.fs)
dyn.run(50)
e_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {e_initial:.4f} eV")
print(f"Final total energy: {e_final:.4f} eV")
