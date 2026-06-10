import numpy as np
from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = {}

for symbol in metals:
    atoms = bulk(symbol, 'fcc', a=4.0, cubic=True)
    atoms.calc = EMT()

    cell0 = atoms.get_cell()
    v0_cell = atoms.get_volume()
    volumes, energies = [], []

    for scale in np.linspace(0.94, 1.06, 9):
        a = atoms.copy()
        a.set_cell(cell0 * scale, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v_eq, e_eq, B = eos.fit()
    a_eq = (4 * v_eq) ** (1/3)  # FCC: 4 atoms per conventional cell

    results[symbol] = {'a_eq': a_eq, 'B_GPa': B * 160.21766208}  # eV/Å³ → GPa

print(f"{'Metal':<6} {'a_eq (Å)':>10} {'B (GPa)':>10}")
print("-" * 28)
for sym, r in results.items():
    print(f"{sym:<6} {r['a_eq']:>10.3f} {r['B_GPa']:>10.1f}")
