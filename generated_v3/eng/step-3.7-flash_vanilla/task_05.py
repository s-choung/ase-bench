from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Generate scaled Cu FCC structures for EOS fitting
cu = bulk('Cu', 'fcc', a=3.6)
scales = [0.95 + 0.1 * i / 9 for i in range(10)]
volumes, energies = [], []
for s in scales:
    cu_s = cu.copy()
    cu_s.set_cell(cu_s.cell * s, scale_atoms=True)
    cu_s.calc = EMT()
    volumes.append(cu_s.get_volume())
    energies.append(cu_s.get_potential_energy())

# Fit EOS and extract properties
eos = EquationOfState(volumes, energies)
v0, _, B = eos.fit()
a0 = v0 ** (1/3)

# Output results
print(f"Equilibrium lattice constant: {a0:.3f} Å")
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B * 160.21766208:.2f} GPa")
