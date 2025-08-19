import tkinter as tk
from tkinter import messagebox


class Calculator(tk.Tk):
    """A simple red & white themed calculator."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Kırmızı Beyaz Hesap Makinesi")
        self.configure(bg="#ff0000")  # red background

        self.expression = ""
        self._build_widgets()

    def _build_widgets(self) -> None:
        entry_frame = tk.Frame(self, bg="#ff0000")
        entry_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.entry = tk.Entry(entry_frame, font=("Arial", 24), bd=5, relief=tk.FLAT, justify=tk.RIGHT)
        self.entry.pack(fill=tk.BOTH)

        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "=", "/",
        ]

        btn_frame = tk.Frame(self, bg="#ff0000")
        btn_frame.pack(padx=10, pady=10)

        for i, char in enumerate(buttons):
            cmd = (lambda ch=char: self._on_button_click(ch))
            btn = tk.Button(
                btn_frame,
                text=char,
                width=5,
                height=2,
                font=("Arial", 18),
                command=cmd,
                bg="#ffffff",
                fg="#000000",
                relief=tk.RAISED,
            )
            btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)

    def _on_button_click(self, char: str) -> None:
        if char == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == "=":
            try:
                result = eval(self.expression, {}, {})
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as exc:  # pylint: disable=broad-except
                messagebox.showerror("Hata", f"Geçersiz ifade: {exc}")
        else:
            self.expression += char
            self.entry.insert(tk.END, char)


def main() -> None:
    app = Calculator()
    app.mainloop()


if __name__ == "__main__":
    main()
