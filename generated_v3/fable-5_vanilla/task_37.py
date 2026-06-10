from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = molecule('N2')
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

potentialenergy = atoms.get_potential_energy()

vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()
vib.summary()

thermo = IdealGasThermo(
    vib_energies=vib_energies,
    potentialenergy=potentialenergy,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0,
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)
print(f"\nPotential energy: {potentialenergy:.6f} eV")
print(f"Gibbs free energy (298.15 K, 1 atm): {G:.6f} eV")
