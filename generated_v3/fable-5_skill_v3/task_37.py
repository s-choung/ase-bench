from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='vib')
vib.run()
vib.summary()
vib_energies = vib.get_energies()
print("Frequencies (cm^-1):", vib.get_frequencies())
vib.clean()

potentialenergy = atoms.get_potential_energy()

thermo = IdealGasThermo(vib_energies=vib_energies,
                        potentialenergy=potentialenergy,
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)
print(f"Gibbs free energy at 298.15 K, 1 atm: {G:.6f} eV")
