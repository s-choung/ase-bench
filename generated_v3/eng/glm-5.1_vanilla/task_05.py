from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

cu = bulk('Cu', 'fcc', a=3.6)
volumes, energies = [], []

for x in [0.95, 0.97, 0.99, 1.0, 1.01, 1.03, 1.05]:
    s = cu.copy()
    s.set_cell(cu.cell * x**(1/3), scale_atoms=True)
    s.calc = EMT()
    volumes.append(s.get_volume())
    energies.append(s.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0:.4f} Å^3")
print(f"Bulk modulus: {B * 160.21766208:.2f} GPa")
