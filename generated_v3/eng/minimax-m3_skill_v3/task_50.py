import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

metals = ['Cu', 'Ag', 'Au']
ref_a = {'Cu': 3.6, 'Ag': 4.1, 'Au': 4.1}  # initial guess
results = []

for metal in metals:
    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 11):
        a = ref_a[metal] * x
        atoms = bulk(metal, 'fcc', a=a)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (4 * v0) ** (1/3)
    results.append((metal, a0, B / units.kbar * 1e-3))  # B in GPa

print(f"{'Metal':<6} {'a0 (Å)':>10} {'B (GPa)':>10}")
print("-" * 28)
for metal, a0, B in results:
    print(f"{metal:<6} {a0:>10.4f} {B:>10.3f}")
