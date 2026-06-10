from ase import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# N2 molecule setup and optimization
n2 = molecule('N2')
n2.calc = EMT()
BFGS(n2).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(n2)
vib.run()
vib_energies = vib.get_energies()
vib.clean()

# Gibbs free energy calculation
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=n2,
                        geometry='linear', symmetrynumber=2, spin=0)
gibbs = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(gibbs)
