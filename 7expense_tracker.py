#07 💸 Expense Tracker
# Crea un rastreador de gastos simple que:
# - Mantenga una lista de gastos
# - Permita agregar nuevos gastos (categoría y monto)
# - Muestre todos los gastos
# - Calcule el total de gastos
# - Genere un informe de gastos por categoría
# - Permita establecer un presupuesto y alerte cuando se exceda


class Gasto:
    def __init__(self, categoria:str, monto:float):
        self.categoria = categoria
        self.monto = monto
class Expense_tracker:

    def __init__(self):
        self.lista=[]

    def agregar_gasto(self, categoria: str, monto: float):
        gasto = Gasto(categoria, monto)
        self.lista.append(gasto)
        print("-------------------")
        print("Gasto agregado con exito :) ")
    
    def mostrar_gastos(self):
        for gasto in self.lista:
            print("-------------------")
            print(f". Categoria: {gasto.categoria} | Monto:{gasto.monto}")
        
    def total_gastos(self):
        total = sum(gasto.monto for gasto in self.lista)
        return total

    def informe(self):
        suma_informe = {}
        for gasto in self.lista:
            if gasto.categoria in suma_informe:
                suma_informe[gasto.categoria] += gasto.monto
            else:
                suma_informe[gasto.categoria] = gasto.monto

        for categoria, total in suma_informe.items():
            print("-------------------")
            print(f"Categoria: {categoria} | monto: {total}")

    def eliminar_ultimo(self):
        self.lista.pop()
        print("-------------------")
        print("Tu ultimo gasto fue elimina con exito")


    def limpiar_lista(self):
        self.lista.clear()
        print("-------------------")
        print("Tu lista fue limpiada con exito, tu lista actualizada:", self.lista)
    

def main():
    tracker = Expense_tracker()
    prendido = True
    presupuesto= float(input("Dame el presupuesto que tienes: ")) 

    while prendido:
        print("-----------------------")
        print("1. Cerrar")
        print("2. Agregar Nuevo Gasto")
        print("3. Todos los gastos")
        print("4. Total de Gastos")    
        print("5. informe de gastos por categoría")
        print("6. Elimina tu ultimo elemnto de la lista")
        print("7. Limpia tu lista por completo")
        
        total_actual = tracker.total_gastos()
        if total_actual > presupuesto:
            print("¡¡¡Ya te pasaste de tu presupeusto!!!!")
        accion = int(input("Inserta el numero de la accion que deseas realizar: ")) 
        if accion == 1:
            print("Se cerro el programa con exito")
            prendido = False
        elif accion == 2:
            categoria = str(input("Inserta el nombre del gasto: "))
            monto = float(input("Inserta el monto del gasto: "))
            tracker.agregar_gasto(categoria, monto)
        elif accion == 3:
            tracker.mostrar_gastos()
        elif accion == 4:
            total= tracker.total_gastos()
            print("-------------------")
            print("Este es el total de tu gastos:", total)
        elif accion == 5:
            tracker.informe()
        elif accion == 6:
            tracker.eliminar_ultimo()
        elif accion == 7:
            tracker.limpiar_lista()
        else:
            print("insertaste un valor erroreo, se cierra el programa por cuestiones de seguridad :( )")
            break

if __name__ ==  "__main__":
    main()