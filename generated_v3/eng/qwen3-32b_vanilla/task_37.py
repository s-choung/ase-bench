from ase.build import Molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = Molecule('N2')
atoms.set_calculator(EMT())
vib = Vibrations(atoms)
vib.run()
freqs_thz = vib.get_frequencies()
freqs_ev = [f * 0.00413567 for f in freqs_thz]
thermo = IdealGasThermo(vibfreqs=freqs_ev, geometry='linear', symmetrynumber=2)
print(thermo.get_gibbs_energy(298.15, 101325))
