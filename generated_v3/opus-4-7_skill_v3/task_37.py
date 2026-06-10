from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = molecule('N2')
atoms.calc = EMT()

BFGS(atoms).run(fmax=0.01)
E_pot = atoms.get_potential_energy()

vib = Vibrations(atoms, name='vib_n2')
vib.run()
vib_energies = vib.get_energies()
vib.summary()

thermo = IdealGasThermo(
    vib_energies=vib_energies,
    potentialenergy=E_pot,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0,
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Potential energy: {E_pot:.4f} eV")
print(f"Gibbs free energy at 298.15 K, 1 atm: {G:.4f} eV")

vib.clean()
