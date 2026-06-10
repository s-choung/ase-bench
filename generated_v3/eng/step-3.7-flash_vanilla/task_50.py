from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []
for m in metals:
    a_vals = np.linspace(3.0, 5.0, 15)
    vols, ens = [], []
    for a in a_vals:
        atoms = bulk(m, 'fcc', a=a)
        atoms.calc = EMT()
        vols.append(atoms.get_volume())
        ens.append(atoms.get_potential_energy())
    eos = EquationOfState(vols, ens)
    v0, _, B = eos.fit()
    B_GPa = B * 160.21766208
    a_eq = v0 ** (1/3)
    results.append((m, a_eq, B_GPa))

print("| Metal | a_eq (Å) | B (GPa) |")
print("|-------|----------|---------|")
for m, a, b in results:
    print(f"| {m}    | {a:.2f}     | {b:.1f}    |")
