import tkinter as tk
from tkinter import messagebox
from rdkit import Chem
from rdkit.Chem import Descriptors, Draw
from PIL import Image, ImageTk

# Function to add functional groups to a molecule
def add_functional_group(mol, fg_smiles, atom_idx):
    try:
        fg = Chem.MolFromSmiles(fg_smiles)
        if fg is None:
            raise ValueError(f"Invalid SMILES for functional group: {fg_smiles}")
        combined = Chem.CombineMols(mol, fg)
        rw_mol = Chem.RWMol(combined)
        rw_mol.AddBond(atom_idx, mol.GetNumAtoms(), Chem.rdchem.BondType.SINGLE)
        return rw_mol.GetMol()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

# Function to check if the molecule is valid
def is_valid_molecule(mol):
    try:
        Chem.SanitizeMol(mol)
        return True
    except:
        return False

# Function to generate a molecule with specific properties
def generate_molecule(base_smiles, functional_groups):
    mol = Chem.MolFromSmiles(base_smiles)
    if mol is None:
        messagebox.showerror("Error", f"Invalid base SMILES: {base_smiles}")
        return None
    
    for fg_smiles, atom_idx in functional_groups:
        mol = add_functional_group(mol, fg_smiles, atom_idx)
        if mol is None or not is_valid_molecule(mol):
            messagebox.showerror("Error", f"Failed to add functional group {fg_smiles} at index {atom_idx}")
            return None
    
    return mol

# Function to display the molecule
def display_molecule(molecule):
    img = Draw.MolToImage(molecule)
    img = ImageTk.PhotoImage(img)
    img_label.configure(image=img)
    img_label.image = img

def generate_and_display():
    base_smiles = base_entry.get()
    functional_groups_input = fg_entry.get().split(',')
    functional_groups = [(fg.split(':')[0], int(fg.split(':')[1])) for fg in functional_groups_input if ':' in fg]
    
    molecule = generate_molecule(base_smiles, functional_groups)
    
    if molecule is None:
        return
    
    mol_weight = Descriptors.MolWt(molecule)
    logp = Descriptors.MolLogP(molecule)
    num_h_donors = Descriptors.NumHDonors(molecule)
    num_h_acceptors = Descriptors.NumHAcceptors(molecule)
    
    result_text = (f"Generated Molecule: {Chem.MolToSmiles(molecule)}\n"
                   f"Molecular Weight: {mol_weight}\n"
                   f"LogP: {logp}\n"
                   f"Number of Hydrogen Donors: {num_h_donors}\n"
                   f"Number of Hydrogen Acceptors: {num_h_acceptors}")
    
    result_label.config(text=result_text)
    display_molecule(molecule)

# Create the main window
root = tk.Tk()
root.title("MolGen")

tk.Label(root, text="Base SMILES:").grid(row=0, column=0)
base_entry = tk.Entry(root)
base_entry.grid(row=0, column=1)

tk.Label(root, text="Functional Groups (SMILES:Index, separated by commas):").grid(row=1, column=0)
fg_entry = tk.Entry(root)
fg_entry.grid(row=1, column=1)

tk.Label(root, text="Desired LogP:").grid(row=2, column=0)
logp_entry = tk.Entry(root)
logp_entry.grid(row=2, column=1)

tk.Label(root, text="Desired Sigma:").grid(row=3, column=0)
sigma_entry = tk.Entry(root)
sigma_entry.grid(row=3, column=1)

tk.Label(root, text="Desired Pi:").grid(row=4, column=0)
pi_entry = tk.Entry(root)
pi_entry.grid(row=4, column=1)

tk.Label(root, text="Desired HBA:").grid(row=5, column=0)
hba_entry = tk.Entry(root)
hba_entry.grid(row=5, column=1)

tk.Label(root, text="Desired HBD:").grid(row=6, column=0)
hbd_entry = tk.Entry(root)
hbd_entry.grid(row=6, column=1)

generate_button = tk.Button(root, text="Generate Molecule", command=generate_and_display)
generate_button.grid(row=7, column=0, columnspan=2)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=8, column=0, columnspan=2)

img_label = tk.Label(root)
img_label.grid(row=9, column=0, columnspan=2)

root.mainloop()
