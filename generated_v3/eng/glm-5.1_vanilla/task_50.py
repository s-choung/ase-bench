from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase import units

metals = ['Cu', 'Ag', 'Au']
results = []

for sym in metals:
    atoms = bulk(sym, 'fcc', a=4.0, cubic=True)
    atoms.calc = EMT()
    eos = calculate_eos(atoms)
    v0, e0, B = eos.fit()
    a0 = v0**(1/3)
    B_GPa = B / units.GPa
    results.append((sym, a0, B_GPa))

print(f"{'Metal':<6} {'Lattice (Å)':<15} {'Bulk Mod. (GPa)':<15}")
print("-" * 36)
for sym, a0, B_GPa in results:
    print(f"{sym:<6} {a0:<15.4f} {B_GPa:<15.2f}")
