from ase.build import mx2
from ase.calculators.emt import EMT

# MoS2 monolayer (2H) with 10 Å vacuum along z
atoms = mx2('Mo', 'S', kind='2H', a=3.160, nlayers=1,
            vacuum=10.0, periodic=False)

atoms.set_calculator(EMT())          # optional built‑in calculator
print('Cell vectors (Å):')
print(atoms.get_cell())
print('Cell lengths (Å):', atoms.get_cell().lengths())
