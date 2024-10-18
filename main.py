import customtkinter as ctk
from tkinter import messagebox
from tkinter import Listbox, Scrollbar
import requests
import json
from tkhtmlview import HTMLLabel
import os

version_app = '1.9'

creditos = '''

    Gracias por usar Security Helpy!

    Desarrollado por: TripleAn
    GitHub: https://github.com/triplean

'''

firt_time_file = 'gracias.txt'
if not os.path.exists(firt_time_file):
    messagebox.showinfo(f"Version {version_app}", f"Security Helpy se ha actualizado a la version {version_app}!")

    with open(firt_time_file, 'w') as f:
        f.write(creditos)

root = ctk.CTk()

class FNAFHelpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Helpy")

        self.create_widgets()
        self.load_posts()

    def create_widgets(self):
        self.buscar_label = ctk.CTkLabel(self.root, text="Busqueda:")
        self.buscar_label.grid(row=0, column=0, padx=3, pady=3)

        self.search_entry = ctk.CTkEntry(self.root, width=300)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        self.search_button = ctk.CTkButton(self.root, text="Buscar", command=self.search_help)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        self.home_button = ctk.CTkButton(self.root, text="Regresar a inicio", command=self.load_highlighted_posts)
        self.home_button.grid(row=0, column=3, padx=10, pady=10)

        self.version_button = ctk.CTkButton(self.root, text="Speedruns", command=self.open_speedrun_version)
        self.version_button.grid(row=0, column=4, padx=10, pady=10)

        self.posts_frame = ctk.CTkFrame(self.root)
        self.posts_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        self.posts_listbox = Listbox(self.posts_frame, width=90, height=20)
        self.posts_listbox.pack(side="left", fill="y")
        self.posts_listbox.bind("<<ListboxSelect>>", self.show_post)

        self.posts_text = HTMLLabel(self.posts_frame, width=100, height=35, background="white")
        self.posts_text.pack(side="right", fill="both", expand=True)

        self.bar_text = Scrollbar(self.posts_frame, orient="vertical", command=self.posts_text.yview)
        self.bar_text.pack(side="right", fill="y")


    def load_posts(self):
        try:
            data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts_es.json"
            response = requests.get(data_url)
            if response.status_code == 200:
                posts = json.loads(response.content.decode("utf-8"))
                for post in posts:
                    self.posts_listbox.insert(ctk.END, post['title'])
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los posts: {str(e)}")

    def load_highlighted_posts(self):
        self.posts_listbox.delete(0, ctk.END)
        try:
            data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts_es.json"
            response = requests.get(data_url)
            if response.status_code == 200:
                posts = json.loads(response.content.decode("utf-8"))
                for post in posts:
                    if post.get('highlighted', False):
                        self.posts_listbox.insert(ctk.END, post['title'])
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los posts destacados: {str(e)}")

    def search_help(self):
        search_term = self.search_entry.get().lower()
        if not search_term:
            messagebox.showwarning("Advertencia", "Por favor ingresa un término de búsqueda.")
            return

        self.posts_listbox.delete(0, ctk.END)
        try:
            data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts_es.json"
            response = requests.get(data_url)
            if response.status_code == 200:
                posts = json.loads(response.content.decode("utf-8"))
                for post in posts:
                    if search_term in post.get('title', '').lower() or search_term in post.get('content', '').lower():
                        self.posts_listbox.insert(ctk.END, post['title'])
                    else:
                        self.posts_listbox.insert(ctk.END, "No encontramos resultados")
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar ayuda: {str(e)}")

    def show_post(self, event):
        selected_index = self.posts_listbox.curselection()
        if selected_index:
            selected_post = self.posts_listbox.get(selected_index)
            try:
                data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts.json"
                response = requests.get(data_url)
                if response.status_code == 200:
                    posts = json.loads(response.content.decode("utf-8"))
                    for post in posts:
                        if post['title'] == selected_post:
                            self.posts_text.set_html(post['html'])
                            break
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar el contenido de la guía: {str(e)}", options="Enviar informe")

    def load_posts_from_speedrun_version(self):
        try:
            data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts_speedrun_es.json"
            response = requests.get(data_url)
            if response.status_code == 200:
                posts = json.loads(response.content.decode("utf-8"))
                self.posts_listbox.delete(0, ctk.END)
                for post in posts:
                    self.posts_listbox.insert(ctk.END, post['title'])
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los posts para speedrunners: {str(e)}")

    def close_main_app(self):
        root.destroy()

    def open_speedrun_version(self):
        messagebox.showinfo("Proximamente", "El modo speedrunner sigue bajo desarrollo.")

def main():
    app = FNAFHelpApp(root)
    root.iconbitmap("logo.ico")
    root.after(0, lambda: root.wm_state('zoomed'))
    root.mainloop()

if __name__ == "__main__":
    main()
