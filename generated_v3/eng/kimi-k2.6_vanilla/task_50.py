from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

symbols = ['Cu', 'Ag', 'Au']
a_guess = {'Cu': 3.6, 'Ag': 4.09, 'Au': 4.08}
results = []

for sym in symbols:
    atoms = bulk(sym, 'fcc', a=a_guess[sym], cubic=True)
    atoms.calc = EMT()
    cell = atoms.get_cell()
    vols, ens = [], []
    for sf in np.linspace(0.95, 1.05, 5):
        atoms.set_cell(cell * sf, scale_atoms=True)
        vols.append(atoms.get_volume())
        ens.append(atoms.get_potential_energy())
    v0, e0, B = EquationOfState(vols, ens).fit()
    a0 = v0 ** (1 / 3)
    B_gpa = B * 160.21766208
    results.append((sym, a0, B_gpa))

print(f"{'Metal':<8} {'a0 (Å)':<12} {'B (GPa)':<12}")
print("-" * 32)
for sym, a0, B_gpa in results:
    print(f"{sym:<8} {a0:<12.4f} {B_gpa:<12.2f}")
