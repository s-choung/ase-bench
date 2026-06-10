from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for symbol in metals:
    atoms = bulk(symbol, 'fcc', a={'Cu':3.6, 'Ag':4.0, 'Au':4.1}[symbol], cubic=True)
    atoms.calc = EMT()
    cell = atoms.get_cell()
    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    B_gpa = B * 160.2177
    results.append((symbol, a0, B_gpa))

print(f"{'Metal':<6} {'a0 (Å)':<10} {'B (GPa)':<10}")
print("-" * 28)
for symbol, a0, B in results:
    print(f"{symbol:<6} {a0:<10.4f} {B:<10.2f}")
