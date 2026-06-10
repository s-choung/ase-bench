import numpy as np
from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from tabulate import tabulate

elements = ['Cu', 'Ag', 'Au']
a_latt = [3.6, 4.1, 4.1]  # Initial guesses
results = []

for elem, a in zip(elements, a_latt):
    atoms = Atoms(elem, cell=[a,a,a], pbc=True)
    atoms.calc = EMT()
    
    vols, ens = [], []
    for s in np.linspace(0.95,1.05,7):
        a_test = atoms.copy()
        a_test.set_cell(a * s, scale_atoms=True)
        vols.append(a_test.get_volume())
        ens.append(a_test.get_potential_energy())
    
    eos = EquationOfState(vols, ens, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a_eq = (4 * v0 / len(atoms))**(1/3)
    results.append([elem, a_eq, B/units.GPa])

print(tabulate(results, headers=["Element", "a₀ (Å)", "Bulk Modulus (GPa)"], floatfmt=".3f", tablefmt="grid"))
