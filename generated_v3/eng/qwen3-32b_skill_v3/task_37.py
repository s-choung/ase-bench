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
freqs = vib.get_frequencies()
vib_energies = freqs / 8065.54429  # cm⁻¹ to eV
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms, geometry='linear', symmetrynumber=2)
g = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(g)
