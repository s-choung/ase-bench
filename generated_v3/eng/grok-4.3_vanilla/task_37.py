from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
atoms = Atoms('N2', [(0,0,0),(0,0,1.1)])
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_vibrational_energies()
thermo = IdealGasThermo(vib_energies=vib_energies, potentialenergy=atoms.get_potential_energy(), atoms=atoms, geometry='linear', symmetrynumber=2, spin=0)
print(thermo.get_gibbs_free_energy(298.15, 101325.))
vib.clean()
