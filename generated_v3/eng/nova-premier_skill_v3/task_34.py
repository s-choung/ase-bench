from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Surface with Cu adatom
slab = fcc111('Cu', (3,3,5), vacuum=10.0)
adatom = Atoms('Cu', [[slab[0].x, slab[0].y, 15]])
slab += adatom

# Create initial/final states
initial, final = slab.copy(), slab.copy()
initial[-1].position += (-0.5, -0.3, 0)
final[-1].position += (+0.5, +0.3, 0)

# Fix bottom layers
mask = [i < 2 for i in range(len(slab))]
initial.set_constraint(FixAtoms(mask))
final.set_constraint(FixAtoms(mask))

# Interpolate 5-image path
images = [initial] + [slab.copy() for _ in range(5)] + [final]
neb = NEB(images, interpolate='idpp')

# Setup calculators
for im in images: im.calc = EMT()

# Optimize pathway
qn = BFGS(neb, trajectory='neb.traj')
qn.run(fmax=0.05)

# Energy barrier calculation
e_barrier = max(neb.get_energies()) - neb.get_potential_energy()
print(f"Energy barrier: {e_barrier:.3f} eV")
