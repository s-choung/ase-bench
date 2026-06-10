from ase.build import fcc111
from ase.md.velocityverlet import VelocityVerlet
from ase.calculators.emt import EMT
import numpy as np

atoms = fcc111('Pd', size=(2, 2, 2), vacuum=1.0)
atoms.set_cell([10.0, 10.0, 10.0], scale=1.0)
atoms.get_potential_energy()

calculator = EMT()
atoms.calc = calculator

temp = 500.0
timestep = 2.0
nsteps = 200

nv = VelocityVerlet(atoms, timestep)
nv.run(nsteps)

initial_energy = atoms.get_potential_energy() + np.sum(atoms.get_kinetic_energy())
final_energy = atoms.get_potential_energy() + np.sum(atoms.get_kinetic_energy())

print(f"Change in total energy: {final_energy - initial_energy:.6f} eV")
