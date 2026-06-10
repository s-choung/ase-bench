from ase.build import bulk
from ase.calculators.emt import EMT
from ase.utils.eos import EquationOfState
import numpy as np

metals = {'Cu': 29, 'Ag': 47, 'Au': 79}
results = []

for symbol, Z in metals.items():
    atoms = bulk(symbol, 'fcc', a=4.0, cubic=True)
    atoms.calc = EMT()
    
    volumes = []
    energies = []
    for strain in np.linspace(0.9, 1.1, 11):
        atoms.set_cell(strain * atoms.cell, scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3) * np.sqrt(2)  # FCC lattice constant
    results.append((symbol, a0, B))

print(f"{'Metal':<5} {'a0 (Å)':>8} {'B (GPa)':>10}")
for metal, a0, B in results:
    print(f"{metal:<5} {a0:8.3f} {B/1e9:10.2f}")
