"""T10 Skill: Fix bottom 2 layers of a 4-layer Pt(111) slab"""
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

c = FixAtoms(indices=[atom.index for atom in slab if atom.position[2] < 5.0])
slab.set_constraint(c)

opt = BFGS(slab)
opt.run(fmax=0.05, steps=10)
print(f"Relaxed. Energy: {slab.get_potential_energy():.4f} eV")
