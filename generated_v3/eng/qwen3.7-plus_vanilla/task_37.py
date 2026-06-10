from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.05)

vib = Vibrations(atoms)
vib.run()

thermo = IdealGasThermo(vib_energies=vib.get_energies(), atoms=atoms, geometry='linear', symmetrynumber=2)
print(thermo.get_gibbs_energy(298.15, 101325.0))
