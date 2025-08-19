RED = "\033[31m"
WHITE = "\033[37m"
WHITE_BG = "\033[47m"
RESET = "\033[0m"

def calculate(expr: str) -> float:
    """Evaluate a simple binary expression like '2 + 2'."""
    tokens = expr.split()
    if len(tokens) != 3:
        raise ValueError("Lütfen 'sayı işlem sayı' formatında girin")
    a_str, op, b_str = tokens
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError as exc:
        raise ValueError("Geçersiz sayı girdiniz") from exc

    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    raise ValueError("Desteklenmeyen işlem")


def main() -> None:
    header = f"{WHITE_BG}{RED}Basit Hesap Makinesi{RESET}"
    print(header)
    while True:
        expr = input(f"{RED}İşlem giriniz (örn: 2 + 2) veya 'çıkış': {RESET}")
        if expr.lower() in {"çıkış", "cikis", "exit", "quit", "q"}:
            print(f"{WHITE_BG}{RED}Hoşçakalın!{RESET}")
            break
        try:
            result = calculate(expr)
            print(f"{WHITE_BG}{RED}Sonuç: {result}{RESET}")
        except Exception as e:  # pylint: disable=broad-exception-caught
            print(f"{WHITE_BG}{RED}Hata: {e}{RESET}")


if __name__ == "__main__":
    main()
