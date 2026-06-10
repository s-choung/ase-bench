from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
vib_energies = [e for e in vib.get_energies() if e.real > 0.01]

thermo = IdealGasThermo(vib_energies, 'linear', atoms=atoms,
                        potentialenergy=atoms.get_potential_energy(),
                        symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)
print(G)
