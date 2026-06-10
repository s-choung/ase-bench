from ase import Atoms
from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.units import Angstrom

# Build Pt(111) 3-layer slab with vacuum
slab = fcc111('Pt', size=(3, 3, 3), vacuum=15.0)

# Add CO adsorbate on top site
co = molecule('CO')
from ase.build import add_adsorbate
add_adsorbate(slab, co, height=1.8, position='ontop')

# Identify indices: bottom layer is first 9 atoms (layer 0), C-O are last 2 atoms
indices_bottom = [a.index for a in slab if a.tag == 0]  # layer 0 atoms
c_idx = len(slab) - 2
o_idx = len(slab) - 1

# Apply constraints simultaneously
constraints = [
    FixAtoms(indices=indices_bottom),
    FixBondLength(a1=c_idx, a2=o_idx)
]
slab.set_constraint(constraints)

# Set calculator and optimize
slab.calc = EMT()
opt = BFGS(slab, trajectory='co_pt111.traj')
opt.run(fmax=0.05)

# Print results
energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_idx, o_idx)
print(f"Final energy: {energy:.6f} eV")
print(f"C-O distance: {co_dist:.4f} Angstrom")
