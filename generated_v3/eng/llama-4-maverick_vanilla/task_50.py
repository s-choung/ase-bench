from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np
from tabulate import tabulate

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    bulk = Atoms(metal, cell=[[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]], pbc=True, scaled_positions=[[0, 0, 0]])
    bulk *= (4, 4, 4)
    bulk.calc = EMT()
    volumes = []
    energies = []
    for a in np.linspace(3.5, 4.5, 9):
        bulk.cell = a * np.eye(3)
        volumes.append(bulk.get_volume())
        energies.append(bulk.get_potential_energy())
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = (v0 / len(bulk) * 4) ** (1/3)
    results.append([metal, f'{a0:.3f}', f'{B/160.2:.1f}'])

print(tabulate(results, headers=['Metal', 'Lattice Constant (Å)', 'Bulk Modulus (GPa)'], tablefmt='orgtbl'))
