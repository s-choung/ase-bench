from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = {"Cu": 3.60, "Ag": 4.09, "Au": 4.08}
scale_factors = [0.94, 0.96, 0.98, 0.99, 1.00, 1.01, 1.02, 1.04, 1.06]

results = []

for sym, a_ref in metals.items():
    volumes, energies = [], []
    for s in scale_factors:
        atoms = bulk(sym, "fcc", a=a_ref * s, cubic=True)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = v0 ** (1.0 / 3.0)
    B_GPa = B * 160.21766208
    results.append((sym, a0, B_GPa))

print(f"{'Metal':<6} {'a0 (Ang)':>12} {'Bulk modulus (GPa)':>20}")
print("-" * 40)
for sym, a0, B in results:
    print(f"{sym:<6} {a0:12.4f} {B:20.2f}")
