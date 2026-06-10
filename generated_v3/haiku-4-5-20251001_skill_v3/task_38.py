from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='vib')
vib.run()

vib_energies = vib.get_energies()

thermo = HarmonicThermo(vib_energies=vib_energies, atoms=atoms)
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz Free Energy at 300K: {F:.6f} eV")

vib.clean()
