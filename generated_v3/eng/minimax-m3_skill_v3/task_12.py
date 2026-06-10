from ase.build import bulk
from ase.io import write

a = 2.95
c = a * 1.59
atoms = bulk('Ti', 'hcp', a=a, c=c)

print("Cell vectors (Angstrom):")
for v in atoms.get_cell():
    print(f"  [{v[0]:.6f}, {v[1]:.6f}, {v[2]:.6f}]")

print("\nAtomic positions (Cartesian, Angstrom):")
for sym, pos in zip(atoms.get_chemical_symbols(), atoms.get_positions()):
    print(f"  {sym}: [{pos[0]:.6f}, {pos[1]:.6f}, {pos[2]:.6f}]")

print("\nAtomic positions (Fractional):")
for sym, frac in zip(atoms.get_chemical_symbols(), atoms.get_scaled_positions()):
    print(f"  {sym}: [{frac[0]:.6f}, {frac[1]:.6f}, {frac[2]:.6f}]")

write('Ti_hcp.cif', atoms)
