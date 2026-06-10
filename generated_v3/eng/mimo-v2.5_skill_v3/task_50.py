import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

metals = {'Cu': 3.65, 'Ag': 4.15, 'Au': 4.12}
results = {}

for sym, a0 in metals.items():
    atoms = bulk(sym, 'fcc', a=a0, cubic=True)
    atoms.calc = EMT()

    cell = atoms.get_cell()
    volumes, energies = [], []
    for scale in np.linspace(0.90, 1.10, 15):
        a = atoms.copy()
        a.set_cell(cell * scale, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a_eq = (4.0 * v0) ** (1.0 / 3.0)
    B_GPa = B / units.kJ * 1e24  # eV/Å³ → GPa: 1 eV/Å³ = 160.2176634 GPa
    B_GPa = B * 160.21766208
    results[sym] = (a_eq, B_GPa)

print(f"{'Metal':>6s} | {'Lattice Const (Å)':>18s} | {'Bulk Modulus (GPa)':>18s}")
print("-" * 50)
for sym in metals:
    a_eq, B_GPa = results[sym]
    print(f"{sym:>6s} | {a_eq:>18.4f} | {B_GPa:>18.2f}")
