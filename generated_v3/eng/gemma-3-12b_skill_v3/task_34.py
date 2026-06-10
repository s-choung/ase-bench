from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB
from ase.geometry import cell
import numpy as np

slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab.calc = EMT()

hollow_hcp = np.array([0.5, 0.5, 0.0])
adatom = {'symbol': 'Cu', 'position': hollow_hcp}

initial_state = slab.copy()
add_adsorbate(initial_state, adatom, height=2.0, position='hcp')
initial_state.set_cell(cell(slab.get_cell()), scale_atoms=True)
initial_energy = initial_state.get_potential_energy()

final_state = slab.copy()
add_adsorbate(final_state, adatom, height=2.0, position='fcc')
final_state.set_cell(cell(slab.get_cell()), scale_atoms=True)

images = [initial_state, initial_state.copy() for _ in range(3)] + [final_state]


neb = NEB(images)
neb.interpolate(method='idpp')
for img in images:
    img.calc = EMT()


opt = BFGS(neb)
opt.run(fmax=0.01)

max_energy = np.max([img.get_potential_energy() for img in images])

energy_barrier = max_energy - initial_energy
print(f"Energy barrier: {energy_barrier}")
