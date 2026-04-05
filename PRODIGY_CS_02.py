"""
PRODIGY_CS_02 - Pixel Manipulation for Image Encryption
Prodigy Infotech Cybersecurity Internship - Task 02
Encrypt and decrypt images using pixel-level XOR operations.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os


def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)
    img.save(output_path)
    return output_path


def decrypt_image(image_path, key, output_path):
    # XOR is its own inverse, so decrypt = encrypt
    return encrypt_image(image_path, key, output_path)


class ImageEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption - PRODIGY_CS_02")
        self.root.geometry("820x600")
        self.root.configure(bg="#0d0d1a")
        self.root.resizable(False, False)
        self.image_path = None
        self.build_ui()

    def build_ui(self):
        # Header
        hdr = tk.Frame(self.root, bg="#0d0d1a")
        hdr.pack(fill='x', padx=30, pady=(22, 0))
        tk.Label(hdr, text="🖼️  Image Encryption Tool", font=("Courier New", 20, "bold"),
                 fg="#ff6b9d", bg="#0d0d1a").pack(side='left')
        tk.Label(hdr, text="PRODIGY_CS_02", font=("Courier New", 9),
                 fg="#444466", bg="#0d0d1a").pack(side='right', pady=(8, 0))

        tk.Frame(self.root, height=1, bg="#1e1e3a").pack(fill='x', padx=30, pady=12)

        # Main layout
        main = tk.Frame(self.root, bg="#0d0d1a")
        main.pack(fill='both', expand=True, padx=30)

        # Left panel - controls
        left = tk.Frame(main, bg="#0d0d1a", width=260)
        left.pack(side='left', fill='y', padx=(0, 20))
        left.pack_propagate(False)

        # File select
        self._section(left, "1. SELECT IMAGE")
        self.file_label = tk.Label(left, text="No file chosen", font=("Courier New", 8),
                                   fg="#555577", bg="#131325", wraplength=220,
                                   justify='left', anchor='w', padx=8, pady=6)
        self.file_label.pack(fill='x', pady=(0, 6))
        self._btn(left, "📂  Browse Image", "#ff6b9d", "#2a0015", self.browse_file).pack(fill='x')

        self._section(left, "2. SET XOR KEY (0–255)")
        self.key_var = tk.IntVar(value=42)
        key_frame = tk.Frame(left, bg="#131325", highlightthickness=1, highlightbackground="#2e2e5e")
        key_frame.pack(fill='x', pady=(0, 6))
        tk.Spinbox(key_frame, from_=0, to=255, textvariable=self.key_var,
                   font=("Courier New", 14, "bold"), bg="#131325", fg="#ff6b9d",
                   relief='flat', buttonbackground="#131325",
                   insertbackground="#ff6b9d", width=8).pack(padx=8, pady=6)

        self._section(left, "3. ACTION")
        self._btn(left, "🔒  ENCRYPT IMAGE", "#ff6b9d", "#1a0010", self.encrypt).pack(fill='x', pady=(0, 8))
        self._btn(left, "🔓  DECRYPT IMAGE", "#00ffcc", "#001a13", self.decrypt).pack(fill='x')

        self._section(left, "STATUS")
        self.status_var = tk.StringVar(value="Awaiting input...")
        tk.Label(left, textvariable=self.status_var, font=("Courier New", 8),
                 fg="#7777aa", bg="#0d0d1a", wraplength=230, justify='left').pack(anchor='w')

        # Right panel - image preview
        right = tk.Frame(main, bg="#111122", highlightthickness=1, highlightbackground="#1e1e3a")
        right.pack(side='left', fill='both', expand=True)

        tk.Label(right, text="PREVIEW", font=("Courier New", 9, "bold"),
                 fg="#333355", bg="#111122").pack(pady=(10, 0))

        self.preview_label = tk.Label(right, text="No image loaded\n\nBrowse an image to begin.",
                                      font=("Courier New", 10), fg="#333355",
                                      bg="#111122")
        self.preview_label.pack(expand=True)

    def _section(self, parent, text):
        tk.Label(parent, text=text, font=("Courier New", 8, "bold"),
                 fg="#555577", bg="#0d0d1a", anchor='w').pack(fill='x', pady=(14, 4))

    def _btn(self, parent, text, fg, bg, cmd):
        b = tk.Button(parent, text=text, font=("Courier New", 9, "bold"),
                      fg=fg, bg=bg, activeforeground=fg, activebackground="#1a1a2e",
                      relief='flat', cursor='hand2', pady=8,
                      highlightthickness=1, highlightbackground=fg, command=cmd)
        return b

    def browse_file(self):
        path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All files", "*.*")]
        )
        if path:
            self.image_path = path
            name = os.path.basename(path)
            self.file_label.config(text=name, fg="#aaaacc")
            self.show_preview(path)
            self.status_var.set(f"Loaded: {name}")

    def show_preview(self, path):
        try:
            img = Image.open(path)
            img.thumbnail((460, 400))
            photo = ImageTk.PhotoImage(img)
            self.preview_label.config(image=photo, text="")
            self.preview_label.image = photo
        except Exception as e:
            self.preview_label.config(text=f"Preview error:\n{e}")

    def encrypt(self):
        self._process("encrypted")

    def decrypt(self):
        self._process("decrypted")

    def _process(self, mode):
        if not self.image_path:
            messagebox.showwarning("No Image", "Please select an image first.")
            return
        key = self.key_var.get()
        base, ext = os.path.splitext(self.image_path)
        out_path = f"{base}_{mode}{ext if ext else '.png'}"
        try:
            if mode == "encrypted":
                encrypt_image(self.image_path, key, out_path)
            else:
                decrypt_image(self.image_path, key, out_path)
            self.show_preview(out_path)
            self.status_var.set(f"✅ {mode.capitalize()} → {os.path.basename(out_path)}")
            messagebox.showinfo("Done", f"Image {mode} successfully!\nSaved to:\n{out_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set(f"❌ Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptionApp(root)
    root.mainloop()
