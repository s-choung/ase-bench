import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

metals = ['Cu', 'Ag', 'Au']
a_guess = {'Cu': 3.6, 'Ag': 4.09, 'Au': 4.08}

results = []
for m in metals:
    atoms = bulk(m, 'fcc', a=a_guess[m], cubic=True)
    cell0 = atoms.get_cell()
    volumes, energies = [], []
    for x in np.linspace(0.94, 1.06, 9):
        a = atoms.copy()
        a.set_cell(cell0 * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 * 4) ** (1/3)
    B_GPa = B / units.kJ * 1.0e24
    results.append((m, a0, B_GPa, e0))

print(f"{'Metal':<6}{'a0 (Å)':>12}{'B (GPa)':>12}{'E0 (eV)':>12}")
print('-' * 42)
for m, a0, B, e0 in results:
    print(f"{m:<6}{a0:>12.4f}{B:>12.2f}{e0:>12.4f}")
