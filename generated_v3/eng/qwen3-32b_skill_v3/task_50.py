import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    initial = bulk(metal, 'fcc', cubic=True)
    x_values = np.linspace(0.95, 1.05, 7)
    volumes, energies = [], []

    for x in x_values:
        scaled = initial.copy()
        scaled.set_cell(initial.cell * x, scale_atoms=True)
        scaled.calc = EMT()
        volumes.append(scaled.get_volume())
        energies.append(scaled.get_potential_energy())

    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    B_gpa = B * 160.21766208
    results[metal] = (a0, B_gpa)

print(f"{'Metal':<10} {'a0 (Å)':<10} {'Bulk Modulus (GPa)':<15}")
for metal in metals:
    a0, B = results[metal]
    print(f"{metal:<10} {a0:.4f} {B:.2f}")
