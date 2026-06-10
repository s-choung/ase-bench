from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.paths import find_saddle
import numpy as np

surfaces = [fcc111('Cu', size=(4, 4, 3), vacuum=10.0)]
adatom = surfaces[0].copy()
adatom.append(np.array([2.0, 2.0, 4.0]))
adatom.set_cell(surfaces[0].get_cell())
adatom.set_positions(surfaces[0].get_positions() + adatom.positions)
adatom.center(vacuum=10.0, axis=2)

hcp_site = surfaces[0].copy()
hcp_site.append(np.array([1.0, 2.0, 5.0]))
hcp_site.set_cell(surfaces[0].get_cell())
hcp_site.set_positions(surfaces[0].get_positions() + hcp_site.positions)
hcp_site.center(vacuum=10.0, axis=2)

images = [adatom.copy(), hcp_site.copy()]
calc = EMT()
neb = NEB(images, calculator=calc, climb=True, kpts=(4, 4, 1), method='IDPP')
neb.interpolate(5)

energies = [image.get_potential_energy() for image in neb]
max_energy = max(energies)
barrier = max_energy - energies[0]

print(f"Energy barrier: {barrier:.3f} eV")
