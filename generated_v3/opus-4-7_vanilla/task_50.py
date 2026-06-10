import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ

metals = ['Cu', 'Ag', 'Au']
a0_guess = {'Cu': 3.6, 'Ag': 4.09, 'Au': 4.08}

results = []
for m in metals:
    a0 = a0_guess[m]
    volumes, energies = [], []
    for s in np.linspace(0.94, 1.06, 9):
        atoms = bulk(m, 'fcc', a=a0 * s)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a_eq = (4 * v0) ** (1/3)
    B_GPa = B / kJ * 1.0e24
    results.append((m, a_eq, B_GPa))

print(f"{'Metal':<6}{'a_eq (Å)':<12}{'B (GPa)':<10}")
print('-' * 28)
for m, a, B in results:
    print(f"{m:<6}{a:<12.4f}{B:<10.2f}")
