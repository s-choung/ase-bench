from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
n2.calc = EMT()

BFGS(n2).run(fmax=0.01)
energy = n2.get_potential_energy()

vib = Vibrations(n2)
vib.run()
vib_energies = vib.get_energies()

thermo = IdealGasThermo(
    vib_energies=vib_energies,
    potentialenergy=energy,
    atoms=n2,
    geometry='linear',
    symmetrynumber=2,
    spin=0,
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)
print('Gibbs free energy (eV):', G)
