from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

atoms = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
atoms.calc = EMT()

c = FixAtoms(mask=[a.tag in (1, 2) for a in atoms])
atoms.set_constraint(c)

fixed = [i for i, a in enumerate(atoms) if a.tag in (1, 2)]
before = atoms.get_positions()[fixed]

BFGS(atoms).run(fmax=0.05)

after = atoms.get_positions()[fixed]

print("Fixed atom indices:", fixed)
for i, idx in enumerate(fixed):
    diff = after[i] - before[i]
    print(f"Atom {idx}: before={before[i]}, after={after[i]}, diff={diff}")
