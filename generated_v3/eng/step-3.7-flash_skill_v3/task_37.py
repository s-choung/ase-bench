from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms, name='n2_vib')
vib.run()
vib_energies = vib.get_energies()[abs(vib.get_energies()) > 1e-5]
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms, geometry='linear', symmetrynumber=2, spin=0)
gibbs = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Gibbs free energy at 298.15 K and 1 atm: {gibbs:.4f} eV")
