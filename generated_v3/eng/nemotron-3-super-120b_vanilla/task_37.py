from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = molecule('N2')
atoms.calc = EMT()
atoms.get_potential_energy()

vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()

thermo = IdealGasThermo(vibrational_energies=vib_energies,
                        potentialenergy=atoms.get_potential_energy(),
                        temperature=298.15,
                        pressure=101325,
                        geometry='linear',
                        symmetrynumber=2)

G = thermo.get_gibbs_energy()
print(f'Gibbs free energy: {G:.4f} eV')
