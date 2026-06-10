import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for sym in metals:
    # initial guess for lattice constant (will be overridden)
    atoms = bulk(sym, 'fcc', a=3.6)
    atoms.calc = EMT()
    V0 = atoms.get_volume()
    # generate a set of volumes around the guess
    vols = np.linspace(0.9, 1.1, 11) * V0
    energies = []
    for v in vols:
        a = v ** (1/3)  # cubic cell: V = a^3
        atm = bulk(sym, 'fcc', a=a, cubic=True)
        atm.calc = EMT()
        energies.append(atm.get_potential_energy())
    # fit to Birch-Murnaghan equation of state
    eos = EquationOfState(vols, energies)
    v_eq, e_eq, B = eos.fit()  # B in eV/Å^3
    a_eq = v_eq ** (1/3)
    B_GPa = B * 160.21766208  # convert eV/Å^3 to GPa
    results.append((sym, a_eq, B_GPa))

# print comparison table
print(f"{'Metal':<5} {'a0 (Å)':>10} {'B0 (GPa)':>12}")
for sym, a, b in results:
    print(f"{sym:<5} {a:10.4f} {b:12.2f}")
