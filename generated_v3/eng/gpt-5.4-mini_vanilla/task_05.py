from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

volumes, energies = [], []
for s in [0.94, 0.96, 0.98, 1.00, 1.02, 1.04, 1.06]:
    a = atoms.copy()
    a.set_cell(atoms.cell * s, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0:.6f} Å^3")
print(f"Bulk modulus: {B:.6f} eV/Å^3")
