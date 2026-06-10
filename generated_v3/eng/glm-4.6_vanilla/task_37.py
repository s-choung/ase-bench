from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase.optimize import BFGS

atoms = Atoms('N2', positions=[[0, 0, -0.55], [0, 0, 0.55]])
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

thermo = IdealGasThermo(vib.get_energies(), atoms.get_potential_energy(),
                        atoms, geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(G)
