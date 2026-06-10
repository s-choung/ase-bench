from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build slab and add CO
slab = fcc111('Pt', size=(3,3,3), vacuum=10.0)
slab.center(axis=2, vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.85, position='ontop')

# Fix bottom layer atoms
zpos = [atom.position[2] for atom in slab]
zmin = min(zpos)
tol = 0.01
mask = [atom.position[2] < zmin + tol for atom in slab]
c1 = FixAtoms(mask=mask)

# Identify C and O indices (after slab atoms)
co_indices = range(len(slab)-2, len(slab))
c_co, o_co = co_indices
c2 = FixBondLength(c_co, o_co)

slab.set_constraint([c1, c2])
slab.calc = EMT()

opt = BFGS(slab, trajectory=None, logfile=None)
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_co, o_co)
print(f'Final energy: {energy:.6f} eV')
print(f'C-O bond length: {co_dist:.4f} Å')
