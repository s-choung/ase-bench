import numpy as np
from ase.build import fcc111
from ase.io import write
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.constraints import FixAtoms

# 1. Setup Surface (Slab)
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()

# 2. Define Initial (fcc) and Final (hcp) positions
# Cu(111) surface sites: fcc and hcp are both hollow sites.
# We place a single Cu adatom on the top layer.
adatom = slab.copy()
# Remove the original top layer atoms to isolate the slab for the adatom
# Or more simply, create a clean slab and add an adatom.
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()

# To find specific sites: fcc is (1/3, 2/3, 1/3) relative to lattice
# For simplicity, we'll use the build tools or manual displacement.
# Let's define initial and final states by taking one atom and moving it.
initial_state = slab.copy()
# Create adatom at an fcc site (approximate)
from ase.build import add_adsorbate
# We use a simple trick: find a hollow site via manual positioning
# For Cu FCC(111), a simple way is to find the coordinate of a hollow site.
# Here we create the initial and final atoms manually for precision.
initial_ads = slab.copy()
# Add an adatom at a specific height
# Note: add_adsorbate modifies in-place.
# Instead, let's just create the adatom Atoms object.
from ase import Atoms
# Define a surface and an adatom
surface = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
surface.calc = EMT()
# Constraint to keep slab fixed
slab_mask = [a.tag < 10 for a in surface] # Example logic, let's use explicit indices
# Better: Define slab and adatom separately
slab_only = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
slab_only.calc = EMT()
# Indices of atoms in the top layer (layer 3)
top_layer_indices = [atom.index for atom in slab_only if atom.position[2] > 5.0] 
# We'll just freeze the bottom layers
constraint = FixAtoms(indices=[atom.index for atom in slab_only if atom.position[2] < 5.0])
slab_only.set_constraint(constraint)

# Define adatom positions (fcc vs hcp)
# In a 3x3 fcc111, we can pick positions relative to the lattice
# For this script, we'll define two slightly different positions for the adatom
# to simulate the jump.
adatom_initial = Atoms('Cu', positions=[[1.5, 1.5, 5.5]]) # Dummy coords
# Let's use the built-in atoms and displace
# A better way to ensure valid sites:
from ase.build import fcc111
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()
# Let's assume the top layer is at z ~ 6.0. 
# We pick an atom from the top layer and move it.
# But the prompt asks for an adatom. Let's add a Cu atom.
def get_hollow_sites(slab):
    # Simplified: just return two points near a hollow site
    # In real usage, one would use symmetry or geometry tools
    z = slab.positions[0][2] + 2.5 # height above surface
    return np.array([[2.0, 2.0, z], [2.5, 2.5, z]])

pos_fcc = np.array([[2.0, 2.0, 7.0]])
pos_hcp = np.array([[2.5, 2.5, 7.0]])

initial = slab.copy()
initial.append(Atoms('Cu', positions=pos_fcc))
initial.calc = EMT()
initial.set_constraint(FixAtoms(indices=[a.index for a in initial if a.position[2] < 6.0]))

final = slab.copy()
final.append(Atoms('Cu', positions=pos_hcp))
final.calc = EMT()
final.set_constraint(FixAtoms(indices=[a.index for a in final if a.position[2] < 6.0]))

# 3. NEB Calculation
n_images = 5
images = [initial] + [initial.copy() for _ in range(n_images)] + [final]

# Assign calculators
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')

# Optimize
opt = BFGS(neb)
opt.run(fmax=0.05)

# 4. Results
e_initial = initial.get_potential_energy()
energies = [img.get_potential_energy() for img in images]
e_max = max(energies)
barrier = e_max - e_initial

print(f"Energy Barrier: {barrier:.4f} eV")
