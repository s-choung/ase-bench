from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = molecule('N2')
atoms.calc = EMT()

vib = Vibrations(atoms, name='n2_vib')
vib.run()
energies = vib.get_energies()
vib.clean()

thermo = IdealGasThermo(
    vib_energies=energies,
    potentialenergy=atoms.get_potential_energy(),
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0,
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)
print(f"Gibbs free energy at 298.15 K and 1 atm: {G:.6f} eV")
