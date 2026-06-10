from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a0 = 4.09
volumes = []
energies = []
for x in range(-5, 6, 1):
    a = a0 * (1 + x / 100)
    ag = Atoms('Ag', scaled_positions=[[0, 0, 0]], cell=[[0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]] * a, pbc=True)
    ag *= (3, 3, 3)
    ag.calc = EMT()
    energies.append(ag.get_potential_energy())
    volumes.append(ag.get_volume() / len(ag))

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0_fit = (v0 * 4) ** (1/3)
print(f"Equilibrium lattice constant: {a0_fit:.3f} Angstrom")
print(f"Bulk modulus: {B * 160.21766208:.2f} GPa")
