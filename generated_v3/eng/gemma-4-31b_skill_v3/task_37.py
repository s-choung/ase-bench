from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Setup N2 molecule and optimize
atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='vib')
vib.run()
vib_energies = vib.get_energies() # Returns energies in eV
vib.clean()

# Thermochemistry calculation
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms, 
                        geometry='linear', symmetrynumber=2, spin=0)
g_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f"Gibbs Free Energy: {g_energy}")
