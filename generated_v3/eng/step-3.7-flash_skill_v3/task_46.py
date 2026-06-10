from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixBondLength

# Build 3-layer Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, a=3.92)
# Add CO adsorbate
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
# Get C and O atom indices
c_idx = next(i for i, a in enumerate(slab) if a.symbol == 'C')
o_idx = next(i for i, a in enumerate(slab) if a.symbol == 'O')
# Apply constraints: fix bottom layer and C-O bond
slab.set_constraint([
    FixAtoms(mask=[a.tag == 0 for a in slab]),
    FixBondLength(c_idx, o_idx)
])
# Set calculator and optimize
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)
# Output results
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
print(f"C-O distance: {slab.get_distance(c_idx, o_idx):.4f} Å")
