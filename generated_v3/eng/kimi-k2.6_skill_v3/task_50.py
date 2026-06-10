import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

data = []
for sym, ag in [('Cu', 3.6), ('Ag', 4.0), ('Au', 4.1)]:
    atoms = bulk(sym, 'fcc', a=ag, cubic=True)
    cell = atoms.get_cell()
    vols, ens = [], []
    for s in np.linspace(0.95, 1.05, 7):
        a = atoms.copy()
        a.set_cell(cell * s, scale_atoms=True)
        a.calc = EMT()
        vols.append(a.get_volume())
        ens.append(a.get_potential_energy())
    v0, e0, B = EquationOfState(vols, ens, eos='birchmurnaghan').fit()
    a0 = v0 ** (1.0 / 3.0)
    B_gp = B * 160.2177
    data.append((sym, a0, B_gp))

print(f"{'Metal':<8} {'a0 (Å)':<10} {'B (GPa)':<10}")
print("-" * 28)
for sym, a0, B_gp in data:
    print(f"{sym:<8} {a0:<10.4f} {B_gp:<10.2f}")
