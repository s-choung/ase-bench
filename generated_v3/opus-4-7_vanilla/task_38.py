from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase.optimize import BFGS
from ase.constraints import UnitCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

opt = BFGS(UnitCellFilter(atoms))
opt.run(fmax=0.001)

vib = Vibrations(atoms, name='vib_cu')
vib.run()
vib_energies = vib.get_energies()

real_energies = [e.real for e in vib_energies if e.real > 0]

thermo = HarmonicThermo(vib_energies=real_energies, potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Vibrational energies (eV): {real_energies}")
print(f"Helmholtz free energy at 300K: {F:.6f} eV")
