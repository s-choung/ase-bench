from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.10)])
atoms.calc = EMT()

dyn = BFGS(atoms, logfile=None)
dyn.run(fmax=0.01)

vib = Vibrations(atoms, name='n2_vib')
vib.run()
frequencies = vib.get_frequencies()
vib.clean()

thermo = IdealGasThermo(
    vib_energies=vib.get_energies(),
    geometry='linear',
    atoms=atoms,
    symmetrynumber=2,
    spin=0
)

gibbs = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0, verbose=True)
print("Vibrational frequencies (cm^-1):", frequencies)
print("Gibbs free energy at 298.15 K, 1 atm (eV):", gibbs)
