from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

# Step 1: Find equilibrium lattice constant using EOS
atoms_bulk = bulk('Cu', 'fcc', a=3.6)
atoms_bulk.calc = EMT()

# Sample energies at different lattice constants
volumes, energies = [], []
for a in np.linspace(3.4, 3.8, 7):
    atoms = atoms_bulk.copy()
    atoms.set_cell(atoms.get_cell() * (a / 3.6), scale_atoms=True)
    atoms.calc = EMT()  # Reassign calculator (ASE requires it)
    e = atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(e)

# Fit EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (v0)**(1/3)  # Lattice parameter from volume

# Step 2: Build and relax (111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, latticeconstant=a0)
slab.calc = EMT()

# Fix bottom 2 layers
mask = [atom.index < 2 * 2 * 2 for atom in slab]  # 2 layers × 2x2 surface
slab.set_constraint(FixAtoms(mask=mask))

# Relax surface
opt = BFGS(slab, trajectory='slab_opt.traj')
opt.run(fmax=0.05)

# Step 3: Print final energy and layer info
print(f'Final energy: {slab.get_potential_energy():.4f} eV')

# Calculate平均 (average in this context) z-coordinates per layer
layers = []
for i in range(4):
    layer_atoms = slab[i*4 : (i+1)*4]  # 2x2 surface = 4 atoms per layer
    z_coords = [atom.z for atom in layer_atoms]
    print(f'Layer {i+1} avg z: {np.mean(z_coords):.2f} Å')
