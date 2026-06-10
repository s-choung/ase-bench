from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ

ag = bulk('Ag', 'fcc', a=4.09)
calc = EMT()
ag.calc = calc

volumes, energies = [], []
for scale in [0.95 + i*0.01 for i in range(7)]:
    cell = ag * (2, 2, 2)
    cell.set_cell(cell.cell * scale, scale_atoms=True)
    energies.append(cell.get_potential_energy())
    volumes.append(cell.get_volume())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4 * v0)**(1/3)
print(f"Equilibrium lattice constant: {a0:.3f} Å")
print(f"Bulk modulus: {B / kJ * 1.0e24:.1f} GPa")
