from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

volumes = []
energies = []
for a in [3.0, 3.2, 3.4, 3.6, 3.8]:
    cu = FaceCenteredCubic(directions=[[0, 1, 1], [1, 0, 1], [1, 1, 0]],
                          symbol='Cu', size=(1, 1, 1), pbc=True)
    cu.calc = EMT()
    cu.cell = [a, a, a]
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0:.2f} Å^3, Bulk modulus: {B:.2f} eV/Å^3")
