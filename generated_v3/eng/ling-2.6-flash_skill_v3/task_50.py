from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

results = []

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = Atoms(symbol, positions=[(0, 0, 0)], cell=np.eye(3) * 4.0, pbc=True)
    atoms.calc = EMT()
    symbols, positions, _ = atoms.get_cell(complete=True)
    volumes = []
    energies = []
    for x in np.linspace(0.92, 1.08, 9):
        a = atoms.copy()
        a.set_cell(symbols * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 ** (1 / 3)) * 2  # FCC lattice constant from cubic cell side
    results.append((symbol, a0, B))

print(f"{'Metal':<6}{'a0 (Å)':<12}{'B (GPa)':<12}")
print("-" * 30)
for sym, a0, B in results:
    print(f"{sym:<6}{a0:<12.4f}{B / 1e9:<12.2f}")
