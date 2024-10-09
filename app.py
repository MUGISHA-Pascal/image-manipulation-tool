import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

class ImageManipulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Manipulation Tool")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Load Image Button
        self.load_button = ttk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=10)

        # Manipulation Buttons
        self.resize_button = ttk.Button(root, text="Resize", command=self.resize_image)
        self.resize_button.pack(pady=5)

        self.rotate_button = ttk.Button(root, text="Rotate", command=self.rotate_image)
        self.rotate_button.pack(pady=5)

        self.gray_button = ttk.Button(root, text="Grayscale", command=self.apply_grayscale)
        self.gray_button.pack(pady=5)

        self.blur_button = ttk.Button(root, text="Gaussian Blur", command=self.apply_blur)
        self.blur_button.pack(pady=5)

        self.save_button = ttk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack(pady=10)

        self.canvas = tk.Canvas(root, bg="#ffffff", width=600, height=400)
        self.canvas.pack(pady=20)

        self.image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.display_image(self.image)

    def display_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        self.canvas.config(width=img_tk.width(), height=img_tk.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.canvas.image = img_tk

    def resize_image(self):
        if self.image is not None:
            width = int(self.image.shape[1] * 0.5)
            height = int(self.image.shape[0] * 0.5)
            resized_image = cv2.resize(self.image, (width, height))
            self.display_image(resized_image)

    def rotate_image(self):
        if self.image is not None:
            rotated_image = cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
            self.display_image(rotated_image)

    def apply_grayscale(self):
        if self.image is not None:
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.display_image(gray_image)

    def apply_blur(self):
        if self.image is not None:
            blurred_image = cv2.GaussianBlur(self.image, (15, 15), 0)
            self.display_image(blurred_image)

    def save_image(self):
        if self.image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                       filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
            if file_path:
                cv2.imwrite(file_path, self.image)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageManipulator(root)
    root.mainloop()
