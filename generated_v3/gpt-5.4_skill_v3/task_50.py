import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    a0_guess = {'Cu': 3.60, 'Ag': 4.09, 'Au': 4.08}[metal]
    atoms0 = bulk(metal, 'fcc', a=a0_guess, cubic=True)
    cell0 = atoms0.get_cell()

    volumes = []
    energies = []
    scales = np.linspace(0.94, 1.06, 9)

    for s in scales:
        atoms = atoms0.copy()
        atoms.set_cell(cell0 * s, scale_atoms=True)
        atoms.calc = EMT()
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a_eq = (v0 / 4.0) ** (1.0 / 3.0)
    B_GPa = B / 160.21766208
    results.append((metal, a_eq, B_GPa, e0))

print(f"{'Metal':<6} {'a_eq (Å)':>12} {'Bulk Modulus (GPa)':>22} {'E0 (eV/cell)':>15}")
print("-" * 60)
for metal, a_eq, B_GPa, e0 in results:
    print(f"{metal:<6} {a_eq:12.4f} {B_GPa:22.2f} {e0:15.6f}")
