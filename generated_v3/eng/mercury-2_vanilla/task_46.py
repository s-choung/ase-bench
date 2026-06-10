from ase.build import fcc111
from ase.atoms import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Pt(111) slab, 2×2 surface cell, 3 layers, 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, periodic=True)

# place CO on a top site
top_atom = slab.get_layer_indices()[-1][0]                # an atom in the top layer
c_pos = slab.positions[top_atom] + (0, 0, 1.5)            # C ≈1.5 Å above surface
o_pos = c_pos + (0, 0, 1.13)                             # O ≈1.13 Å above C
co = Atoms('CO', positions=[c_pos, o_pos])
atoms = slab + co

# constraints: fix bottom layer and the C‑O bond length
fix_bottom = FixAtoms(indices=slab.get_layer_indices()[0])
c_idx, o_idx = len(slab), len(slab) + 1
fix_bond = FixBondLength(c_idx, o_idx)
atoms.set_constraint([fix_bottom, fix_bond])

# calculation and geometry optimisation
atoms.set_calculator(EMT())
BFGS(atoms).run(fmax=0.05)

# results
print(f'Final energy: {atoms.get_potential_energy():.3f} eV')
print(f'C‑O distance: {atoms.get_distance(c_idx, o_idx):.3f} Å')
