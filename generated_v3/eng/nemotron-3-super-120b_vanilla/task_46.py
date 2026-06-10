from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.lennardjones import LennardJones

# Pt(111) slab, 3 layers, 2x2 surface
slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)
Npt = len(slab)

# CO molecule
co = molecule('CO')
# place CO on top of a Pt atom in the top layer (tag == 2)
top_pt = next(atom for atom in slab if atom.tag == 2)
co.translate(top_pt.position - co.get_center_of_mass() + [0,0,2.0])

# combine slab and CO
slab += co   # now slab contains Pt + C + O

# constraints: fix bottom layer (tag == 0) and fix C-O bond
bottom_mask = [atom.tag == 0 for atom in slab[:Npt]] + [False]*len(slab[Npt:])
constraints = [
    FixAtoms(mask=bottom_mask),
    FixBondLength(indices=[Npt, Npt+1],
                  length=slab.get_distance(Npt, Npt+1))
]
slab.set_constraint(constraints)

# simple Lennard-Jones calculator (same sigma/epsilon for all pairs)
slab.calc = LennardJones(sigma=3.0, epsilon=0.01)

# geometry optimization
opt = BFGS(slab)
opt.run(fmax=0.05)

# results
energy = slab.get_potential_energy()
co_distance = slab.get_distance(Npt, Npt+1)
print(f'Final energy: {energy:.3f} eV')
print(f'C-O distance: {co_distance:.3f} Å')
