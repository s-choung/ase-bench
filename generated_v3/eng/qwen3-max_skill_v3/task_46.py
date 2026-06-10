from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create Pt(111) slab with 3 layers and vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Add CO adsorbate on top site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Set constraints
# Fix bottom layer (atoms with tag == 3)
fix_bottom = FixAtoms(mask=[a.tag == 3 for a in slab])
# Fix C-O bond (last two atoms: C and O)
fix_co = FixBondLength(len(slab) - 2, len(slab) - 1)
slab.set_constraint([fix_bottom, fix_co])

# Set calculator and optimize
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Get results
energy = slab.get_potential_energy()
co_distance = slab.get_distance(len(slab) - 2, len(slab) - 1)

print(f"Final energy: {energy:.6f} eV")
print(f"C-O distance: {co_distance:.6f} Å")
