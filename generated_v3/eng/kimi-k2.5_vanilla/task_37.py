from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
atoms.calc = EMT()

QuasiNewton(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
vib_energies = [e.real for e in vib.get_energies() if e.imag == 0 and e.real > 0.01]

thermo = IdealGasThermo(vib_energies=vib_energies, geometry='linear', 
                        symmetrynumber=2, atoms=atoms)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(G)
