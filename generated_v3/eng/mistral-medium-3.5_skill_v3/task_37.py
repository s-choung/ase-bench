from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import units

atoms = Atoms('N2', positions=((0, 0, 0), (0, 0, 1.1)))
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
vib_energies = vib.get_energies()
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms,
                        geometry='linear', symmetrynumber=2)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=1*units.atm)
print(f'Gibbs free energy: {G:.4f} eV')
