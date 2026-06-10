from ase import Atom, Atoms
from ase.build import surface
from ase.calculators import kernelpolish

fcc_cell = [[3.92, 0., 0.], [0., 3.92, 0.], [0., 0., 3.92]]
Pt = surface(fcc_cell, 'Pt', (4, 4, 1),('.111',))
Pt.vacuum = 10.0

adsorbed = Pt.copy()
adsorbed.append(Atom('C', (0, 0, 2.0)))
adsorbed.append(Atom('O', (0, 0, 2.8)))

kernelpolish(adsorbed, 0.1)
print(len(adsorbed.atoms))
