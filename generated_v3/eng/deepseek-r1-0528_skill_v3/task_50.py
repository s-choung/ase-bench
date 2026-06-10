import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

results = {}
metals = ['Cu', 'Ag', 'Au']
a0_initial = [3.6, 4.1, 4.1]
for symbol, a0 in zip(metals, a0_initial):
    atoms = bulk(symbol, 'fcc', a=a0)
    volumes = []
    energies = []
    for x in np.linspace(0.95, 1.05, 7):
        scaled = atoms.copy()
        scaled.set_cell(atoms.cell * x, scale_atoms=True)
        scaled.calc = EMT()
        volumes.append(scaled.get_volume())
        energies.append(scaled.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B, _ = eos.fit()
    a0_eq = (4 * v0) ** (1/3)
    results[symbol] = (a0_eq, B * 160.217662)

print("Metal | a₀ (Å) | B (GPa)")
print("------|--------|---------")
for metal in metals:
    a, B = results[metal]
    print(f"{metal:5} | {a:.4f} | {B:.1f}")
