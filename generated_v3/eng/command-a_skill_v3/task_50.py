from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = {'Cu': 3.6, 'Ag': 4.1, 'Au': 4.1}  # Initial guesses for lattice constant
results = []

for symbol, a0 in metals.items():
    atoms = bulk(symbol, 'fcc', a=a0, cubic=True)
    atoms.calc = EMT()
    
    cell = atoms.get_cell()
    volumes, energies = [], []
    
    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a_eq = v0 ** (1/3) * a0 / (a0**3) ** (1/3)  # Equilibrium lattice constant
    results.append((symbol, a_eq, B/units.GPa))

print(f"{'Metal':<4}  {'a0 (Å)':>7}  {'Bulk Modulus (GPa)':>16}")
for metal, a, B in results:
    print(f"{metal:<4}  {a:7.3f}  {B:16.2f}")
