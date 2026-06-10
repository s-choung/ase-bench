from ase.build import bcc110

fe_surface = bcc110('Fe', size=(2, 2, 4), vacuum=10.0, a=2.86)
print(f"Number of atoms: {len(fe_surface)}")
print(f"Cell dimensions (Å): {fe_surface.cell.lengths()}")
