from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# H2 분자 생성
atoms = Atoms('H2', positions=[[0, 0, 0], [0.74, 0, 0]])
atoms.calc = EMT()

# constraint 적용 전
energy_before = atoms.get_potential_energy()
bond_length_before = atoms.get_distance(0, 1)
print(f"Before constraint:")
print(f"  Bond length: {bond_length_before:.4f} Å")
print(f"  Energy: {energy_before:.6f} eV")

# FixBondLength constraint 적용
constraint = FixBondLength(0, 1)
atoms.set_constraint(constraint)

# constraint 적용 후
energy_after = atoms.get_potential_energy()
bond_length_after = atoms.get_distance(0, 1)
print(f"\nAfter FixBondLength constraint (0.74 Å):")
print(f"  Bond length: {bond_length_after:.4f} Å")
print(f"  Energy: {energy_after:.6f} eV")

# 0.9 Å로 고정
atoms.set_distance(0, 1, 0.9)
atoms.set_constraint(FixBondLength(0, 1))
energy_fixed = atoms.get_potential_energy()
bond_length_fixed = atoms.get_distance(0, 1)
print(f"\nWith bond length fixed to 0.9 Å:")
print(f"  Bond length: {bond_length_fixed:.4f} Å")
print(f"  Energy: {energy_fixed:.6f} eV")
