import sys

def verifica_echipa():
    nume_echipa = "Bobocii UTCN" # Puteti schimba numele aici
    print(f"--- Salutare de la {nume_echipa}! ---")
    print(f"Python ruleaza de la adresa: {sys.executable}")
    print(f"Versiunea folosita: {sys.version}")
    print("---------------------------------------")

if __name__ == "__main__":
    verifica_echipa()