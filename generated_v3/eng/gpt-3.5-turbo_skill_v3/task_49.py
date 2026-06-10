from ase.build import fcc111, add_adsorbate
from ase.io import write
from ase.io.trajectory import Trajectory
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

from ase.eos import EquationOfState
import numpy as np

# Find equilibrium lattice constant of Cu FCC bulk using EOS
from ase.build import bulk
atoms_bulk = bulk('Cu', 'fcc', a=3.6)
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    atoms = atoms_bulk.copy()
    atoms.set_cell(atoms.get_cell() * x, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = (v0**(1/3))

# Create (111) 4-layer slab with the equilibrium lattice constant
slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)

# Attach EMT and fix the bottom 2 layers
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[atom.index < len(slab)//2 for atom in slab]))

# Run BFGS surface relaxation
opt = BFGS(slab, trajectory='surface_opt.traj')
opt.run(fmax=0.05)

# Print final energy and average z-coordinate for each layer
final_energy = slab.get_potential_energy()
layers_z = [atom.position[2] for atom in slab]
layers_count = 4
layer_size = len(layers_z) // layers_count
for i in range(layers_count):
    avg_z = np.mean(layers_z[i*layer_size: (i+1)*layer_size])
    print(f'Layer {i+1} - Average z-coordinate: {avg_z} Å')
print(f'Final Energy: {final_energy} eV')

# Save the trajectory
write('surface_opt.xyz', slab, format='extxyz')
