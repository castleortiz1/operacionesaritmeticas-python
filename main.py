import operaciones_basicas as ob
import operaciones_intermedias as oi
import operaciones_avanzadas as oa

def main():
    print("Operaciones Básicas")
    print("Suma: 5 + 3 =", ob.suma(5, 3))
    print("Resta: 5 - 3 =", ob.resta(5, 3))
    print("Multiplicación: 5 * 3 =", ob.multiplicacion(5, 3))
    print("División: 5 / 3 =", ob.division(5, 3))
    print()

    print("Operaciones Intermedias")
    print("Potencia: 2 ^ 3 =", oi.potencia(2, 3))
    print("Raíz Cuadrada: √16 =", oi.raiz_cuadrada(16))
    print("Módulo: 10 % 3 =", oi.modulo(10, 3))
    print("División Entera: 10 // 3 =", oi.division_entera(10, 3))
    print()

    print("Operaciones Avanzadas")
    print("Seno de 30° =", oa.seno(30))
    print("Coseno de 60° =", oa.coseno(60))
    print("Tangente de 45° =", oa.tangente(45))
    print("Logaritmo base 2 de 8 =", oa.logaritmo(2, 8))

if __name__ == "__main__":
    main()
