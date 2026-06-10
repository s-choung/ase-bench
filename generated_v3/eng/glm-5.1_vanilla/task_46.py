from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
add_adsorbate(slab, molecule('CO'), height=1.5, position='fcc')

c1 = FixAtoms(indices=range(9))  # Bottom layer of 3x3 slab
c2 = FixBondLength(27, 28)       # C and O are the last two atoms
slab.set_constraints([c1, c2])

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.4f} eV")
print(f"C-O distance: {slab.get_distance(27, 28):.4f} Å")
