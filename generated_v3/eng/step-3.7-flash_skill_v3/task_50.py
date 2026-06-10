from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
a_guess = {'Cu': 3.6, 'Ag': 4.09, 'Au': 4.08}
scan_factors = np.linspace(0.95, 1.05, 7)
results = {}

for m in metals:
    atoms = bulk(m, 'fcc', a=a_guess[m], cubic=True)
    base_cell = atoms.cell.copy()
    volumes, energies = [], []
    for x in scan_factors:
        scaled = atoms.copy()
        scaled.set_cell(base_cell * x, scale_atoms=True)
        scaled.calc = EMT()
        volumes.append(scaled.get_volume())
        energies.append(scaled.get_potential_energy())
    v0, _, B = EquationOfState(volumes, energies, eos='birchmurnaghan').fit()
    results[m] = {
        'a0': v0 ** (1/3),
        'B': B * 160.217  # Convert eV/Å³ to GPa
    }

print(f"{'Metal':<6} | {'Lattice Constant (Å)':<20} | {'Bulk Modulus (GPa)':<18}")
print("-" * 50)
for m, data in results.items():
    print(f"{m:<6} | {data['a0']:<20.4f} | {data['B']:<18.2f}")
