import numpy as np
from ase.build import fcc111, add_adatom
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS
from ase.interpolate import IDPP

# 1. Setup System
a = 3.61  # Cu lattice constant
slab = fcc111(size=(3, 3, 3), vacuum=10.0, a=a)
slab.calc = EMT()

# Define initial (fcc hollow) and final (hcp hollow) positions
# In fcc111, hollow sites are at (1/3, 1/3, 0) relative to basis
# We'll find the hollow sites by shifting the adatom
init_pos = [1.5, 1.5, 0.0] # Placeholder logic for finding site
# Simplified: Manually define coordinates for Cu adatom
# Let's use a specific vector for the shift
fcc_hollow = [1.0, 1.0, 0.0] 
hcp_hollow = [1.0, 1.333, 0.0] # Approximation of the shift

# Create Initial State
atoms_i = slab.copy()
add_adatom(atoms_i, position=fcc_hollow, symbol='Cu')
atoms_i.positions[atoms_i.get_number_of_atoms()-1, 2] += 1.0 # Lift off surface
atoms_i.calc = EMT()
# Fix slab atoms
mask = [atom.tag <= slab.get_number_of_atoms() for atom in atoms_i]
atoms_i.set_constraint(FixAtoms(mask=mask))

# Create Final State
atoms_f = slab.copy()
add_adatom(atoms_f, position=hcp_hollow, symbol='Cu')
atoms_f.positions[atoms_f.get_number_of_atoms()-1, 2] += 1.0
atoms_f.calc = EMT()
atoms_f.set_constraint(FixAtoms(mask=mask))

# 2. NEB Setup
n_images = 5
images = [atoms_i.copy() for _ in range(n_images)]
for img in images:
    img.calc = EMT()
    img.set_constraint(FixAtoms(mask=mask))

# IDPP Interpolation
neb = NEB(images)
neb.interpolate(method='idpp', initial=atoms_i, final=atoms_f)

# 3. Optimization
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# 4. Results
energies = [img.get_potential_energy() for img in images]
initial_energy = atoms_i.get_potential_energy()
barrier = max(energies) - initial_energy

print(f"Initial Energy: {initial_energy:.4f} eV")
print(f"Max Energy:     {max(energies):.4f} eV")
print(f"Energy Barrier: {barrier:.4f} eV")
