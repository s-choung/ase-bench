from ase.build import fcc111, add_adsorbate
from ase.calculators import EMT, LJ
from ase.constraints import FixAtoms
from ase.io import write

alc = fcc111('Al', size=(4, 4, 4), a=3.3, cubic=True)
alc.set_calculator(EMT())
alc.add_adsorbate(height=3.0, position='top')
alc.add_constraint(FixAtoms(mask=[alc.get_selection()['Al'][0]]))
alc.calc = LJ()
print(alc.cell)
print(alc.formula)
write('Al_BCC.xyz', alc)
