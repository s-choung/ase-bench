import numpy as np
from ase import Atoms, units
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Find equilibrium lattice constant
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
cell = atoms.get_cell()
volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 7):
    atoms.set_cell(cell * x, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = atoms.get_cell()[0, 0]
print(f"Equilibrium lattice constant: {a_eq:.3f} Å")

# Create (111) 4-layer slab
slab = fcc111('Cu', size=(1, 1, 4), vacuum=10.0, a=a_eq)
slab.calc = EMT()

# Fix the bottom 2 layers
mask = [atom.tag >= 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Run BFGS surface relaxation
opt = BFGS(slab)
opt.run(fmax=0.05)

# Print final energy and average z-coordinate for each layer
final_energy = slab.get_potential_energy()
print(f"Final energy: {final_energy:.4f} eV")

layer_indices = [atom.tag for atom in slab]
layers = set(layer_indices)
for layer in layers:
    layer_atoms = slab[[atom.index for atom in slab if atom.tag == layer]]
    avg_z = np.mean(layer_atoms.get_positions()[:, 2])
    print(f"Layer {layer}: Average z = {avg_z:.3f} Å")
