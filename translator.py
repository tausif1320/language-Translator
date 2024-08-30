import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Define a dictionary for common language shortcuts
language_shortcuts = {
    'english': 'en',
    'spanish': 'es',
    'french': 'fr',
    'german': 'de',
    'chinese': 'zh-cn',
    'japanese': 'ja',
    'korean': 'ko',
    'hindi': 'hi',
    'arabic': 'ar',
    'portuguese': 'pt',
    'russian': 'ru',
    'italian': 'it',
    'dutch': 'nl',
    'greek': 'el',
    'turkish': 'tr',
    'polish': 'pl',
    'swedish': 'sv',
    'thai': 'th',
    'vietnamese': 'vi',
    'hebrew': 'iw'
}

def translate_text(text, src_language, dest_language):
    try:
        translator = Translator()
        
        # Validate and convert language shortcuts to codes
        src_language_code = language_shortcuts.get(src_language.lower(), src_language)
        dest_language_code = language_shortcuts.get(dest_language.lower(), dest_language)
        
        if src_language_code not in LANGUAGES or dest_language_code not in LANGUAGES:
            return "Unsupported language code."
        
        translation = translator.translate(text, src=src_language_code, dest=dest_language_code)
        return translation.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def on_translate():
    text = text_entry.get("1.0", tk.END).strip()
    src_language = src_lang_combobox.get().strip().lower()
    dest_language = dest_lang_combobox.get().strip().lower()
    
    translated_text = translate_text(text, src_language, dest_language)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, translated_text)

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Create and place widgets
tk.Label(root, text="Enter text to translate:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
text_entry = tk.Text(root, height=5, width=40)
text_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Source language:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
src_lang_combobox = ttk.Combobox(root, values=list(language_shortcuts.keys()))
src_lang_combobox.grid(row=2, column=1, padx=10, pady=5)
src_lang_combobox.set("english")

tk.Label(root, text="Target language:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
dest_lang_combobox = ttk.Combobox(root, values=list(language_shortcuts.keys()))
dest_lang_combobox.grid(row=3, column=1, padx=10, pady=5)
dest_lang_combobox.set("spanish")

translate_button = tk.Button(root, text="Translate", command=on_translate)
translate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Translated text:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
result_text = tk.Text(root, height=5, width=40)
result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
