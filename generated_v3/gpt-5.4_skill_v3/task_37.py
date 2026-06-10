from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = molecule('N2')
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='n2_vib')
vib.run()
freqs = vib.get_frequencies()
vib_energies = vib.get_energies()

thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)

print('Frequencies (cm^-1):')
print(freqs)
print('Vibrational energies (eV):')
print(vib_energies)
print(f'Gibbs free energy at 298.15 K and 1 atm: {G:.6f} eV')

vib.clean()
