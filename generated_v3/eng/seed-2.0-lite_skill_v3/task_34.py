from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.constraints import FixAtoms

# Build Cu(111) slab template (3x3 lateral size, 4 atomic layers, 12Å vacuum)
slab_template = fcc111('Cu', size=(3,3,4), vacuum=12.0, a=3.615)
# Fix bottom two atomic layers to prevent bulk relaxation
fix_constraint = FixAtoms(mask=[atom.tag < 3 for atom in slab_template])

# Initial state: Cu adatom at fcc hollow site
slab_initial = slab_template.copy()
cu_adatom = Atoms('Cu', positions=[[0,0,0]])
add_adsorbate(slab_initial, cu_adatom, height=2.0, position='fcc')
slab_initial.set_constraint(fix_constraint)
slab_initial.calc = EMT()
BFGS(slab_initial).run(fmax=0.05)

# Final state: Cu adatom at adjacent hcp hollow site
slab_final = slab_template.copy()
add_adsorbate(slab_final, cu_adatom, height=2.0, position='hcp')
slab_final.set_constraint(fix_constraint)
slab_final.calc = EMT()
BFGS(slab_final).run(fmax=0.05)

# Set up NEB with 5 intermediate images, IDPP interpolation
images = [slab_initial] + [slab_initial.copy() for _ in range(5)] + [slab_final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Assign calculators to all intermediate images
for img in images[1:-1]:
    img.calc = EMT()

# Optimize the reaction path
BFGS(neb).run(fmax=0.05)

# Calculate and print energy barrier
energies = [img.get_potential_energy() for img in images]
energy_barrier = max(energies) - energies[0]
print(f"Diffusion energy barrier: {energy_barrier:.3f} eV")
