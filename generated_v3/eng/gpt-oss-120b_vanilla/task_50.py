from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = {"Cu": 3.62, "Ag": 4.09, "Au": 4.08}  # approximate lattice params (Å)
results = {}

for el, a0 in metals.items():
    atoms = bulk(el, "fcc", a=a0)
    atoms.calc = EMT()
    # generate volumes by scaling lattice constant
    scales = np.linspace(0.94, 1.06, 9)      # ±6 % around a0
    volumes, energies = [], []
    for s in scales:
        atoms.set_cell(atoms.get_cell() * s, scale_atoms=True)
        energies.append(atoms.get_potential_energy())
        volumes.append(atoms.get_volume())
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()                  # B in eV/Å³
    a_eq = (4 * v0)**(1/3)                 # fcc: V = a³/4 → a = (4V)^(1/3)
    B_GPa = B * 160.21766208               # convert to GPa
    results[el] = (a_eq, B_GPa)

# print comparison table
header = f"{'Metal':<5} {'a₀ (Å)':>10} {'B (GPa)':>10}"
print(header)
print("-" * len(header))
for el, (a_eq, B_GPa) in results.items():
    print(f"{el:<5} {a_eq:10.4f} {B_GPa:10.2f}")
