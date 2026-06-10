import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', cubic=True)
    atoms.calc = EMT()
    cell = atoms.get_cell()
    volumes, energies = [], []
    for f in np.linspace(0.95, 1.05, 7):
        scaled = atoms.copy()
        scaled.set_cell(cell * f, scale_atoms=True)
        scaled.calc = EMT()
        volumes.append(scaled.get_volume())
        energies.append(scaled.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    B_GPa = B * 160.2176634  # eV/Å³ to GPa
    results.append((metal, a0, B_GPa))

print(f"{'Metal':<6} {'a0 (Å)':<10} {'B (GPa)'}")
for metal, a0, B in results:
    print(f"{metal:<6} {a0:.4f} {B:.2f}")
