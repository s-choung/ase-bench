from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]], cell=[10, 10, 10], pbc=False)
n2.calc = EMT()

vib = Vibrations(n2)
vib.run()

thermo = IdealGasThermo(
    vib_energies=vib.get_energies(),
    geometry='linear',
    atoms=n2,
    symmetrynumber=2,
    spin=0
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)
print(f"Gibbs Free Energy: {G:.4f} eV")
