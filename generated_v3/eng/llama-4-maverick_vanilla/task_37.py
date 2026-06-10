from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermo import IdealGasThermo

n2 = Atoms('N2', [(0, 0, 0), (0, 0, 1.1)])
n2.calc = EMT()
vib = Vibrations(n2)
vib.run()
vib_energies = vib.get_energies()

thermo = IdealGasThermo(vib_energies=vib_energies, 
                        geometry='linear', 
                        atoms=n2, 
                        symmetrynumber=2, 
                        spin=0)

gibbs_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(gibbs_energy)
