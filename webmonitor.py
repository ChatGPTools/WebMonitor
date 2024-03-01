import tkinter as tk
from tkinter import scrolledtext, filedialog
import requests
import hashlib
import time
from datetime import datetime
from threading import Thread
import difflib

class WebMonitorApp:
    def __init__(self, master):
        self.master = master
        master.title("Web Monitor App")
        master.geometry("600x400")

        self.state = False
        self.save_path = tk.StringVar(master, value="Seleziona cartella...")
        self.contenuto_precedente = ""

        # Configurazione UI
        config_frame = tk.Frame(master)
        config_frame.pack(padx=10, pady=10, fill='x')

        log_frame = tk.Frame(master)
        log_frame.pack(padx=10, pady=10, fill='both', expand=True)

        tk.Label(config_frame, text="URL:").grid(row=0, column=0, sticky='e')
        self.url_entry = tk.Entry(config_frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=5)

        tk.Label(config_frame, text="Intervallo (sec):").grid(row=1, column=0, sticky='e')
        self.interval_entry = tk.Entry(config_frame, width=20)
        self.interval_entry.grid(row=1, column=1, sticky='w', padx=5)

        self.save_path_button = tk.Button(config_frame, text="Scegli Cartella", command=self.scegli_cartella)
        self.save_path_button.grid(row=2, column=1, sticky='w', padx=5)
        self.save_path_label = tk.Label(config_frame, textvariable=self.save_path)
        self.save_path_label.grid(row=2, column=1, sticky='w', padx=120)

        self.start_button = tk.Button(config_frame, text="Avvia Monitoraggio", command=self.avvia_monitoraggio)
        self.start_button.grid(row=3, column=1, sticky='e', padx=5)
        self.stop_button = tk.Button(config_frame, text="Ferma Monitoraggio", command=self.ferma_monitoraggio, state=tk.DISABLED)
        self.stop_button.grid(row=3, column=1, sticky='e', padx=150)

        self.output_text = scrolledtext.ScrolledText(log_frame, state='disabled', height=10)
        self.output_text.pack(padx=5, pady=5, fill='both', expand=True)

    def scegli_cartella(self):
        directory = filedialog.askdirectory()
        if directory:
            self.save_path.set(directory)

    def calcola_hash(self, contenuto):
        return hashlib.sha256(contenuto.encode('utf-8')).hexdigest()

    def confronta_e_salva(self, contenuto_attuale, primo_salvataggio):
        if primo_salvataggio:
            differenze = contenuto_attuale
        else:
            differenze = ''.join(difflib.unified_diff(self.contenuto_precedente.splitlines(keepends=True),
                                                      contenuto_attuale.splitlines(keepends=True),
                                                      fromfile='precedente', tofile='attuale', lineterm='\n'))
        if differenze.strip():  # Evita di salvare file se non ci sono differenze significative
            self.salva_modifiche(differenze)

    def salva_modifiche(self, differenze):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_file = f"{self.save_path.get()}/modifica_{timestamp}.txt"
        with open(nome_file, "w") as file:
            file.write(differenze)
        self.log(f"Salvato {nome_file} con le modifiche rilevate.")

    def log(self, messaggio):
        self.output_text.configure(state='normal')
        self.output_text.insert(tk.END, messaggio + "\n")
        self.output_text.configure(state='disabled')
        self.output_text.yview(tk.END)

    def monitora(self):
        URL = self.url_entry.get()
        INTERVALLO = int(self.interval_entry.get())
        hash_precedente = ""

        while self.state:
            try:
                risposta = requests.get(URL)
                hash_attuale = self.calcola_hash(risposta.text)
                
                if hash_attuale != hash_precedente:
                    self.confronta_e_salva(risposta.text, hash_precedente == "")
                    hash_precedente = hash_attuale
                    self.contenuto_precedente = risposta.text
                
                time.sleep(INTERVALLO)
            except Exception as e:
                self.log(f"Errore: {e}")
                self.state = False

    def avvia_monitoraggio(self):
        if not self.url_entry.get() or not self.interval_entry.get():
            self.log("Inserisci URL e intervallo.")
            return
        if self.save_path.get() == "Seleziona cartella...":
            self.log("Scegli una cartella di salvataggio.")
            return
        self.state = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.thread = Thread(target=self.monitora, daemon=True)
        self.thread.start()
        self.log("Monitoraggio avviato.")

    def ferma_monitoraggio(self):
        self.state = False
        self.log("Ferma monitoraggio in corso...")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.log("Monitoraggio fermato.")

root = tk.Tk()
app = WebMonitorApp(root)
root.mainloop()
