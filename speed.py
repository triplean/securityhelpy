import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import json
from tkhtmlview import HTMLLabel
from ttkthemes import ThemedStyle
from pypresence import Presence

root = tk.Tk()


class FNAFHelpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Helpy Speedruns")


        style = ThemedStyle(self.root)
        style.set_theme("plastik")


        self.create_widgets()
        self.load_posts()
    

    def create_widgets(self):
        self.search_txt = tk.Label(self.root, text="Buscar:")
        self.search_entry = tk.Entry(self.root, width=40)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        self.search_button = ttk.Button(self.root, text="Buscar", command=self.search_help)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        self.home_button = ttk.Button(self.root, text="Regresar a inicio", command=self.load_highlighted_posts)
        self.home_button.grid(row=0, column=3, padx=10, pady=10)

        self.version_button = ttk.Button(self.root, text="Edición común", command=self.open_normal_version)
        self.version_button.grid(row=0, column=4, padx=10, pady=10)

        self.posts_frame = ttk.Frame(self.root)
        self.posts_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        self.posts_listbox = tk.Listbox(self.posts_frame, width=90, height=20)
        self.posts_listbox.pack(side="left", fill="y")
        self.posts_listbox.bind("<<ListboxSelect>>", self.show_post)

        self.posts_text = HTMLLabel(self.posts_frame, width=100, height=35, background="white")
        self.posts_text.pack(side="right", fill="both", expand=True)
    
        self.scrollbar = tk.Scrollbar(self.posts_frame, orient="vertical", command=self.posts_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.posts_text.configure(yscrollcommand=self.scrollbar.set)

    def load_posts(self):
        try:
            data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts_speedrun_es.json"
            response = requests.get(data_url)
            if response.status_code == 200:
                posts = json.loads(response.content.decode("utf-8"))
                for post in posts:
                    self.posts_listbox.insert(tk.END, post['title'])
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los posts: {str(e)}")

    def load_highlighted_posts(self):
        self.posts_listbox.delete(0, tk.END)
        try:
            data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts_speedrun_es.json"
            response = requests.get(data_url)
            if response.status_code == 200:
                posts = json.loads(response.content.decode("utf-8"))
                for post in posts:
                    if post.get('highlighted', False):
                        self.posts_listbox.insert(tk.END, post['title'])
        
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los posts destacados: {str(e)}")
        

    def search_help(self):
        search_term = self.search_entry.get().lower()
        if not search_term:
            messagebox.showwarning("Advertencia", "Por favor ingresa un término de búsqueda.")
            return
        

        self.posts_listbox.delete(0, tk.END)
        try:
            data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts_speedrun_es.json"
            response = requests.get(data_url)
            if response.status_code == 200:
                posts = json.loads(response.content.decode("utf-8"))
                for post in posts:
                    if search_term in post.get('title', '').lower() or search_term in post.get('content', '').lower():
                        self.posts_listbox.insert(tk.END, post['title'])
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar ayuda: {str(e)}")

    def show_post(self, event):
        selected_index = self.posts_listbox.curselection()
        if selected_index:
            selected_post = self.posts_listbox.get(selected_index)
            try:
                data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts_speedrun_es.json"
                response = requests.get(data_url)
                if response.status_code == 200:
                    posts = json.loads(response.content.decode("utf-8"))
                    for post in posts:
                        if post['title'] == selected_post:
                            self.posts_text.set_html(post['html'])
                            break
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar el contenido del post: {str(e)}")        


    def load_posts_from_speedrun_version(self):
        try:
            data_url = "https://triplean.github.io/projects/SecurityHelpy/resources/posts_speedrun_es.json"
            response = requests.get(data_url)
            if response.status_code == 200:
                posts = json.loads(response.content.decode("utf-8"))
                self.posts_listbox.delete(0, tk.END)
                for post in posts:
                    self.posts_listbox.insert(tk.END, post['title'])
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los posts para speedrunners: {str(e)}")
    
    def open_normal_version(self):
        from subprocess import call
        call(["SecurityHelpy.exe"])


def main():
    app = FNAFHelpApp(root)
    root.state("zoomed")
    root.iconbitmap("logo_speed.ico")
    root.mainloop()


if __name__ == "__main__":
    main()