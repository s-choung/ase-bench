from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for sym in metals:
    # initial FCC bulk with a rough guess
    atoms = bulk(sym, 'fcc', a=3.6)
    atoms.calc = EMT()
    vol, energies = [], []
    for s in np.linspace(0.96, 1.04, 7):
        a = atoms.copy()
        a.set_cell(a.get_cell() * s, scale_atoms=True)
        vol.append(a.get_volume())
        energies.append(a.get_potential_energy())
    eos = EquationOfState(vol, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    B_GPa = B * units.GPa
    results.append((sym, a0, B_GPa))

print(f"{'Metal':<6} {'a0 (Å)':>10} {'B0 (GPa)':>12}")
for sym, a0, B in results:
    print(f"{sym:<6} {a0:10.4f} {B:12.2f}")
