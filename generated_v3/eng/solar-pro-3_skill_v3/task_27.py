from ase import Atoms
from ase.calculators.emt import EMT
from ase.md import langevin_bussi as LB
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# build Ag FCC 2x2x2 supercell
ag = Atoms(symbols='Ag'*32, cell=[[4.05,0,0],[0,4.05,0],[0,0,4.05]], pbc=True)
ag.calc = EMT()

# thermalize
MaxwellBoltzmannDistribution(ag, temperature_K=500)
LB(ag, timestep=5*LB.fs, temperature_K=500).run(200)

# monitor temperature
print('step   temperature [K]')
for i in range(0, 200, 50):
    print(i, ag.get_temperature())
