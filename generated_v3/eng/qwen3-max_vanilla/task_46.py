from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create Pt(111) slab with 3 layers
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()

# Add CO adsorbate at hollow site
add_adsorbate(slab, 'CO', height=1.5, position='hollow')

# Identify atom indices
Pt_atoms = [atom.index for atom in slab if atom.symbol == 'Pt']
C_index = len(Pt_atoms)
O_index = C_index + 1

# Fix bottom Pt layer (z < middle of slab)
z_positions = slab.positions[:, 2]
z_mid = (z_positions[Pt_atoms].min() + z_positions[Pt_atoms].max()) / 2
fix_indices = [i for i in Pt_atoms if slab.positions[i, 2] < z_mid]
constraints = [FixAtoms(indices=fix_indices), FixBondLength(C_index, O_index)]

slab.set_constraint(constraints)

# Optimize
opt = BFGS(slab, fmax=0.05)
opt.run()

# Print results
final_energy = slab.get_potential_energy()
co_distance = slab.get_distance(C_index, O_index)
print(f"Final energy: {final_energy:.6f} eV")
print(f"C-O distance: {co_distance:.6f} Å")
