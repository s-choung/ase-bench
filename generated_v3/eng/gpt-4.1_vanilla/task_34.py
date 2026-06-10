from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB, interpolate
from ase.optimize import BFGS
import numpy as np

# Build Cu(111) slab
slab = fcc111('Cu', size=(3,3,4), a=3.615, vacuum=7.0)
slab.set_calculator(EMT())
slab.positions[:,2] -= slab.positions[:,2].min()
slab.center(axis=2, vacuum=7.0)

# Adatom at fcc hollow
fcc = slab.copy()
add_adsorbate(fcc, 'Cu', height=1.8, position='fcc')
fcc.calc = EMT()

# Adatom at hcp hollow
hcp = slab.copy()
add_adsorbate(hcp, 'Cu', height=1.8, position='hcp')
hcp.calc = EMT()

# NEB images via IDPP interpolation
images = [fcc]
for i in range(3):
    img = fcc.copy()
    img.set_calculator(EMT())
    images.append(img)
images.append(hcp)
neb = NEB(images)
interpolate(images, method='idpp')

# NEB calculation
for img in images:
    img.calc = EMT()
opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05)

# Energies
energies = np.array([img.get_potential_energy() for img in images])
energy_barrier = energies.max() - energies[0]
print("Energy barrier: %.3f eV" % energy_barrier)
