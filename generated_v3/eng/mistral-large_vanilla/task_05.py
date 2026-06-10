from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
cu.calc = EMT()

volumes = []
energies = []
for a in [3.5 + i*0.05 for i in range(10)]:
    cu.set_cell(cu.cell * (a / 3.6), scale_atoms=True)
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0:.3f} Å³/atom")
print(f"Bulk modulus: {B / kJ * 1e24:.2f} GPa")
