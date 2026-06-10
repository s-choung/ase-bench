from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ

metals = ["Cu", "Ag", "Au"]
scales = [0.94, 0.97, 1.00, 1.03, 1.06]

print(f"{'Metal':<6} {'a0 (A)':>10} {'B (GPa)':>10}")

for metal in metals:
    atoms0 = bulk(metal, "fcc")
    a_ref = atoms0.cell.lengths()[0]

    volumes, energies = [], []
    for s in scales:
        atoms = bulk(metal, "fcc", a=a_ref * s)
        atoms.calc = EMT()
        energies.append(atoms.get_potential_energy())
        volumes.append(atoms.get_volume())

    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()

    a0 = v0 ** (1 / 3)
    B_GPa = B / kJ * 1.0e24

    print(f"{metal:<6} {a0:10.4f} {B_GPa:10.2f}")
