from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EOSFit
import numpy as np

metals = {
    "Cu": 3.60,
    "Ag": 4.09,
    "Au": 4.08,
}
results = []

for name, a0 in metals.items():
    a_vals = np.linspace(0.94 * a0, 1.06 * a0, 7)
    vols, engs = [], []
    for a in a_vals:
        atoms = bulk(name, "fcc", a=a, cubic=True)
        atoms.set_calculator(EMT())
        engs.append(atoms.get_potential_energy())
        vols.append(atoms.get_volume() / len(atoms))
    v0, e0, B = EOSFit(vols, engs).fit()
    a_eq = (4 * v0) ** (1 / 3)
    B_GPa = B * 160.21766208
    results.append((name, a_eq, B_GPa))

print(f"{'Metal':<5} {'a0 (Å)':>10} {'B (GPa)':>10}")
for m, a, B in results:
    print(f"{m:<5} {a:>10.4f} {B:>10.1f}")
