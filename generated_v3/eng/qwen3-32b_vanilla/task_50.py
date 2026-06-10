from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = {}

for symbol in metals:
    atoms = bulk(symbol, 'fcc')
    volumes, energies = [], []
    for scale in np.linspace(0.95, 1.05, 7):
        atoms_s = atoms.copy()
        atoms_s.set_cell(atoms_s.get_cell() * scale, scale=True)
        atoms_s.calc = EMT()
        energies.append(atoms_s.get_potential_energy())
        volumes.append(atoms_s.get_volume())
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    results[symbol] = (a0, B)

print(f"{'Element':<6} {'a0 (Å)':<10} {'B0 (GPa)':<10}")
for symbol in metals:
    a0, B0 = results[symbol]
    print(f"{symbol:<6} {a0:.3f} {B0:.3f}")
