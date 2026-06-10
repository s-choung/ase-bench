from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
print(f"{'Metal':<8} {'a0 (A)':<12} {'B0 (GPa)':<12}")
print("-" * 32)

for m in metals:
    atoms = bulk(m, 'fcc', a=4.0)
    atoms.calc = EMT()
    eos = EquationOfState(atoms)
    v0, e0, b0, b1 = eos.fit()
    a0 = v0 ** (1.0 / 3.0)
    b0_gpa = b0 * 160.21766208
    print(f"{m:<8} {a0:<12.4f} {b0_gpa:<12.2f}")
