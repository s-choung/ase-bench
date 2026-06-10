from ase.spacegroup import crystal
from ase.io import write, read

nacl = crystal(
    symbols=["Na", "Cl"],
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90],
)

write("NaCl.cif", nacl, format="cif")
atoms = read("NaCl.cif", format="cif")

sg = atoms.info.get("spacegroup", "unknown")
print("Spacegroup:", sg)
print("Number of atoms:", len(atoms))
