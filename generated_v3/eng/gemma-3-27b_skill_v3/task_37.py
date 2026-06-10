from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.09)])
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='N2_vibrations')
vib.run()
frequencies = vib.get_frequencies()
vib.clean()  # Release memory

thermo = IdealGasThermo(vib_energies=frequencies, atoms=atoms,
                        geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f"Gibbs free energy (G): {G:.3f} eV")
