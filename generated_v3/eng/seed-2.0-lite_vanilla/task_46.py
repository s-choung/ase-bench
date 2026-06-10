from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build 3-layer Pt(111) 3x3 slab with 10Å vacuum
slab = fcc111('Pt', size=(3,3,3), a=3.98, vacuum=10.0)

# Add CO molecule atop a surface Pt atom
top_surface_pt = slab[18]  # First atom of the top Pt layer
co = molecule('CO')
# Position C atom 2Å above the surface Pt, O oriented upward
co.translate((top_surface_pt.x - co[0].x,
              top_surface_pt.y - co[0].y,
              top_surface_pt.z + 2.0 - co[0].z))
slab.extend(co)

# Apply dual constraints
fix_bottom_layer = FixAtoms(indices=list(range(9)))  # First 9 atoms = bottom Pt layer
fix_co_bond = FixBondLength(27, 28)  # C at 27, O at 28 after extending slab
slab.set_constraints([fix_bottom_layer, fix_co_bond])

# Run optimization
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output results
print(f"Final total energy: {slab.get_potential_energy():.3f} eV")
print(f"Final C-O bond length: {slab.get_distance(27,28):.3f} Å")
