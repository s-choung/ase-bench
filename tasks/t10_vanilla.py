"""T10 Vanilla: Fix bottom 2 layers of a 4-layer Pt(111) slab"""
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

bottom_indices = [i for i in range(len(slab)) if slab.positions[i, 2] < 5.0]
from ase.constraints import FixAtoms
slab.set_constraint(FixAtoms(indices=bottom_indices))

opt = BFGS(slab)
opt.run(fmax=0.05, steps=10)
print(f"Relaxed. Energy: {slab.get_potential_energy():.4f} eV")
print(f"Fixed atoms: {len(bottom_indices)}")
