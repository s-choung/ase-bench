from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()[5:]
vib.clean()
thermo = IdealGasThermo(vib_energies, atoms, geometry='linear', symmetrynumber=2, spin=0)
print(thermo.get_gibbs_energy(298.15, 101325))
