from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name='n2_vib')
vib.run()
frequencies = vib.get_frequencies()
vib.clean()

thermo = IdealGasThermo(
    vib_energies=frequencies,
    geometry='linear',
    atoms=atoms,
    symmetrynumber=2,
    spin=0
)

gibbs = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)
print("Vibrational frequencies (cm^-1):", frequencies)
print("Gibbs free energy at 298.15 K and 1 atm (eV):", gibbs)
