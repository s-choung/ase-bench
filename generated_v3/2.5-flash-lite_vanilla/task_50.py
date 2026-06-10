from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.parallel import parprint
import numpy as np

elements = ['Cu', 'Ag', 'Au']
results = {}

for element in elements:
    atoms = fcc111(element, size=(2, 2, 2), vacuum=10.0)
    atoms.calc = EMT()

    eos = calculate_eos(atoms, npoints=10,
                         வரம்புகள்=[0.8, 1.2])
    vols, energies = eos.get_்களின்_energies()
    eos.plot(show_plot=False)

    v0 = eos.get_equilibrium_volume()
    e0 = eos.get_minimum_energy()
    bm = eos.get_bulk_modulus()

    results[element] = {
        'lattice_constant': np.cbrt(v0 / 4.0) * 2.0,
        'bulk_modulus': bm
    }

parprint("Element | Lattice Constant (Å) | Bulk Modulus (GPa)")
parprint("------- | ------------------- | ------------------")
for element, data in results.items():
    parprint(f"{element:<7} | {data['lattice_constant']:<20.4f} | {data['bulk_modulus']:.2f}")
