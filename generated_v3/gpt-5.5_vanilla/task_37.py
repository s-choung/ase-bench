from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import units
import tempfile

atoms = molecule("N2")
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)
e_pot = atoms.get_potential_energy()

with tempfile.TemporaryDirectory() as tmp:
    vib = Vibrations(atoms, name=f"{tmp}/vib")
    vib.run()
    vib_energies = vib.get_energies()
    vib.clean()

thermo = IdealGasThermo(
    vib_energies=vib_energies,
    geometry="linear",
    potentialenergy=e_pot,
    atoms=atoms,
    symmetrynumber=2,
    spin=0,
)

g = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)
print("Vibrational energies (eV):", vib_energies)
print("Gibbs free energy at 298.15 K, 1 atm (eV):", g)
