from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermodynamics import IdealGasThermo

n2 = molecule('N2')
n2.calc = EMT()

BFGS(n2).run(fmax=0.001)

vib = Vibrations(n2)
vib.run()
vib_energies = vib.get_energies()

thermo = IdealGasThermo(vib_energies, geometry='linear', symmetrynumber=2, atoms=n2)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f"Gibbs free energy: {G:.6f} eV")
