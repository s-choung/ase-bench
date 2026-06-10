from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np


a0 = 3.61  # Approximate value, will be refined by EOS

atoms = bulk('Cu', 'fcc', a=a0)
atoms.calc = EMT()

# EOS fit to determine the equilibrium lattice constant
volumes = []
energies = []
v0 = atoms.get_volume()
volumes.append(v0)
energies.append(atoms.get_potential_energy())
for x in np.linspace(0.95, 1.05, 7):
    new_cell = atoms.get_cell() * x
    atoms.set_cell(new_cell, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

from ase.eos import EquationOfState
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Create slab with the refined lattice constant
a = (v0 / atoms.get_number_of_atoms())**(1/3)
slab = bulk('Cu', 'fcc', a=a, size=(2, 2, 4))
slab.calc = EMT()

# Fix bottom 2 layers
fix_indices = [atom.index for atom in slab if atom.position[2] < a / 2]
slab.set_constraint(FixAtoms(mask=[atom.index in fix_indices for atom in slab]))


# Relax the slab using BFGS
opt = BFGS(slab, trajectory='cu_slab.traj')
opt.run(fmax=0.02)


# Print final energy and average z-coordinate for each layer
print("Final Energy:", slab.get_potential_energy())

z_coords = [atom.position[2] for atom in slab]
layer_avg_z = []
for i in range(4):
    layer_indices = [atom.index for atom in slab if i * (a / 2) <= atom.position[2] < (i + 1) * (a / 2)]
    layer_z_coords = [z_coords[idx] for idx in layer_indices]
    layer_avg_z.append(np.mean(layer_z_coords))

print("Average z-coordinate for each layer:", layer_avg_z)
