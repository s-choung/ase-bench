import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0)
    cell = atoms.get_cell()
    volumes, energies = [], []

    for x in np.linspace(0.9, 1.1, 11):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    # FCC: V = a^3 / 4 => a = (4 * V)^(1/3)
    a0 = (4 * v0) ** (1.0 / 3.0)
    # B returned in eV/Ang^3, convert to GPa
    B_GPa = B * 160.21766208
    results[metal] = (a0, B_GPa)

print(f"{'Metal':<6} {'a0 (Å)':<12} {'B (GPa)':<12}")
print("-" * 30)
for metal in metals:
    a0, B_GPa = results[metal]
    print(f"{metal:<6} {a0:<12.4f} {B_GPa:<12.2f}")
