from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixBondLength

# Pt(111) slab with vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
# Add CO molecule
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Fix bottom layer (first 4 atoms)
c1 = FixAtoms(range(4))
# Fix C-O bond (last two atoms)
c2 = FixBondLength(len(slab) - 2, len(slab) - 1)
slab.set_constraints([c1, c2])
slab.calc = EMT()

# Optimization
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output results
print("Final Energy [eV]:", slab.get_potential_energy())
print("C-O Distance [Å]:", slab.get_distance(len(slab) - 2, len(slab) - 1))
