import tkinter as tk
import random

class IceCreamFlavorGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Ice Cream Flavor Generator")
        
      
        self.root.configure(bg='lightblue')
        
        self.base_flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint", "Coffee", "Caramel", "Lemon", "Blueberry","guava","mango"]
        self.outlandish_ingredients = ["Pickle", "Bacon", "Sriracha", "Avocado", "Garlic", "Olive", "Cheddar Cheese", "Wasabi"]
        
        self.title_label = tk.Label(root, text="Welcome to the Ice Cream Flavor Generator!", font=("Helvetica", 16), bg='orange')
        self.title_label.pack(pady=20)
        
        self.generate_button = tk.Button(root, text="Generate Flavor", command=self.generate_flavor, font=("Helvetica", 14))
        self.generate_button.pack(pady=20)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), bg='lightgreen')
        self.result_label.pack(pady=20)
        
    def generate_flavor(self):
        base_flavor = random.choice(self.base_flavors)
        outlandish_ingredient = random.choice(self.outlandish_ingredients)
        
        flavor = f"Try this outrageous flavor: {base_flavor} with {outlandish_ingredient} swirl!"
        self.result_label.config(text=flavor)

if __name__ == "__main__":
    root = tk.Tk()
    app = IceCreamFlavorGeneratorApp(root)
    root.mainloop()
