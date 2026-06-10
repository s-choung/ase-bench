from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()
vib.clean()

thermo = IdealGasThermo(vib_energies=vib_energies, 
                        potentialenergy=atoms.get_potential_energy(),
                        atoms=atoms,
                        geometry='linear', 
                        symmetrynumber=2,
                        spin=0)

gibbs_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)
print(f'Gibbs free energy at 298.15 K and 1 atm: {gibbs_energy:.6f} eV')
