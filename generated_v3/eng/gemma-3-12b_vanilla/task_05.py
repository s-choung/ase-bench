from ase.build import fcc
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.calculators.emt import EMT

atoms = fcc('Cu', size=3)
atoms.set_constraint(FixAtoms(mask=[True, False, False, False, False, False]))

calc = EMT()
atoms.calc = calc

volumes = [atoms.get_volume() * scale for scale in [0.8, 0.9, 1.0, 1.1, 1.2]]
energies = [atoms.calc.results['energy'] for atoms in [atoms.copy() for _ in range(len(volumes))]]

eos = EquationOfState(volumes, energies, eos_function='birch')
eos.fit()

volume_equilibrium = eos.volume
bulk_modulus = eos.B

print(f'Equilibrium volume: {volume_equilibrium}')
print(f'Bulk modulus: {bulk_modulus}')
