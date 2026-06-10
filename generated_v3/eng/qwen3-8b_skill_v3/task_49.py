import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.build import fcc111
from ase.optimize import BFGS

# Step 1: Calculate equilibrium lattice constant for Cu FCC
initial_a = 3.6
volumes = []
energies = []
for scale in np.linspace(0.9, 1.1, 7):
    atoms = bulk('Cu', 'fcc', a=initial_a * scale, cubic=True)
    atoms.calc = EMT()
    atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
equilibrium_a = v0 ** (1/3)

# Step 2: Create (111) 4-layer slab
slab = fcc111('Cu', size=(1, 1, 4), vacuum=10.0, a=equilibrium_a)

# Step 3: Attach EMT calculator
slab.calc = EMT()

# Step 4: Fix bottom 2 layers
positions = slab.get_positions()
z_coords = positions[:, 2]
sorted_indices = np.argsort(z_coords)
mask = np.zeros(len(slab), dtype=bool)
mask[:len(sorted_indices)//2] = True  # Approximate bottom 2 layers
slab.set_constraint(FixAtoms(mask=mask))

# Step 5: Run BFGS optimization
opt = BFGS(slab)
opt.run(fmax=0.05)

# Step 6: Print results
final_energy = slab.get_potential_energy()
print(f"Final energy: {final_energy:.6f} eV")

positions = slab.get_positions()
z_coords = positions[:, 2]
sorted_indices = np.argsort(z_coords)
layer_indices = np.array_split(sorted_indices, 4)
layer_averages = [np.mean(z_coords[indices]) for indices in layer_indices]
print(f"Layer z-averages: {layer_averages}")
