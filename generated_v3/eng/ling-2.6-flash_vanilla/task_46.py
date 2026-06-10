```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.build import fcc111, add_adsorbate
from ase.geometry import surface

# Create Pt(111) slab
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0, orthogonal=False)

# Fix bottom layer
num_fixed = sum(1 for atom in slab if atom.position[2] < 1.0)
slab.constraints = [FixAtoms(indices=[i for i, atom in enumerate(slab) if atom.position[2] < 1.0])]

# Add CO adsorbate on top site
co = add_adsorbate(slab, 'CO', atop='top', height=1.5)

# Set EMT calculator
slab.set_calculator(EMT())

# Fix C-O bond length
c_index = len(slab) - 2
o_index = len(slab) - 1
slab.constraints.append(FixBondLength(c_index, o_index))

# Optimize with BFGS
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

# Print results
co_distance = slab.get_distance(c_index, o_index)
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
print(f"C-O distance: {co_distance:.4f} Å")
