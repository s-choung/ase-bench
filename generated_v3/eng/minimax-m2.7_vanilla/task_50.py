from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
calc = EMT()
results = {}

for metal in metals:
    a_vals = np.linspace(3.0, 5.0, 30)
    volumes, energies = [], []
    for a in a_vals:
        atoms = bulk(metal, 'fcc', a=a)
        atoms.calc = calc
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(np.array(volumes), np.array(energies))
    v0, e0, B = eos.fit()                     # B in eV/Å³
    a_eq = (4 * v0) ** (1 / 3)               # cubic lattice constant
    B_GPa = B * 160.217662                    # convert to GPa
    results[metal] = (a_eq, B_GPa)

# Print comparison table
print(f"{'Metal':<8} {'a_eq (Å)':<14} {'B (GPa)':<12}")
print('-' * 38)
for metal, (a_eq, B_GPa) in results.items():
    print(f"{metal:<8} {a_eq:<14.4f} {B_GPa:<12.2f}")
