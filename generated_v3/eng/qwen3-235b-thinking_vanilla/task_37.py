from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.001)

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

thermo = IdealGasThermo(vib_energies=freqs,
                        potentialenergy=atoms.get_potential_energy(),
                        temperature=298.15,
                        pressure=1.0,
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2)
print(thermo.get_gibbs_energy())
