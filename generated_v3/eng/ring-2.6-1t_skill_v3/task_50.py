from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for m in metals:
    atoms = bulk(m, 'fcc', a=3.6, cubic=True)
    atoms.calc = EMT()
    cell0 = atoms.get_cell()
    volumes, energies = [], []
    for s in np.linspace(0.92, 1.08, 9):
        a = atoms.copy()
        a.set_cell(cell0 * s, scale_atoms=True)
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()  # B in eV/Ang^3
    a0 = v0 ** (1 / 3)
    B_GPa = B * 160.21766208
    results.append((m, a0, B_GPa))

print(f"{'Metal':<6} {'a0 (Ang)':<12} {'B (GPa)':<12}")
print("-" * 30)
for m, a0, B in results:
    print(f"{m:<6} {a0:>10.4f}   {B:>10.2f}")
