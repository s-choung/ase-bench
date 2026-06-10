from ase.build import fcc111
from ase.atom import Atom
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.io import write
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import CrystalThermo

# Al(111) slab: 3 layers, 2x2 surface, vacuum 10 Å
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
slab.cell[2,2] = 1.0  # orthorhombic to keep vacuum direction orthogonal
slab.pbc = (True, True, False)  # periodic in-plane only

# adsorb N2 on bridge site (relative position (0.5, 0.5, 1.5) from Al layer)
n2 = molecule('N2')               # N2 molecule
add_adsorbate(slab, n2, height=2.0, position='bridge')  # in‑place

# set a constraint to keep everything except adsorbate free
slab.set_constraint(FixAtoms(mask=[a.tag < n2[0].tag for a in slab]))

# EMT calculator
slab.calc = EMT()

# structural relaxation using BFGS with cell optimization
opt = BFGS(FrechetCellFilter(slab))
opt.run(fmax=0.02)

# Analyze final structure
print(f"Number of atoms: {len(slab)")
# atom types: count identical tags (periodic boundary conditions)
tags = slab.get_tags()
unique_tags = sorted(set(tags))
print(f"Atom types: {unique_tags}")
print(f"Slab formula: Al{_sub}...? Actually tag order matters. Provide a more readable output:")

# Count each species
species = []
for tag in unique_tags:
    species.append(slab.select_atoms(by='tag', criterion=lambda a, t: a.tag == t).symbols)
print(f"Species: {species}")
print(f"Al count: {species[0].count('Al')}")
print(f"N count: {sum([s.count('N') for s in species])}\n")

# optional: output POSCAR (VASP format)
write('slab_POSCAR', slab, format='vasp')
