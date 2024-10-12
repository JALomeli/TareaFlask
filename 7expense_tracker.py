#07 💸 Expense Tracker
# Crea un rastreador de gastos simple que:
# - Mantenga una lista de gastos
# - Permita agregar nuevos gastos (categoría y monto)
# - Muestre todos los gastos
# - Calcule el total de gastos
# - Genere un informe de gastos por categoría
# - Permita establecer un presupuesto y alerte cuando se exceda

from flask import Flask, render_template, request, redirect, url_for, flash

app=Flask(__name__)
app.secret_key="llavesupersecreta"
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
        flash(f"Gasto agregado con exito :) , Categoria: {categoria} | Monto: ${monto}")
    
    def mostrar_gastos(self):
        return self.lista
    
        
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
        return suma_informe


    # def eliminar_ultimo(self):
    #     self.lista.pop()
    #     print("-------------------")
    #     print("Tu ultimo gasto fue elimina con exito")


    # def limpiar_lista(self):
    #     self.lista.clear()
    #     print("-------------------")
    #     print("Tu lista fue limpiada con exito, tu lista actualizada:", self.lista)
    
tracker = Expense_tracker()

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/agregar_gasto", methods=["GET", "POST"])
def agregar_gasto():
    if request.method== "POST":
        categoria = request.form["categoria"]
        monto = float(request.form["monto"])
        tracker.agregar_gasto(categoria,monto)
        return redirect(url_for("index"))
    return render_template("agregar_gasto.html")

@app.route("/mostrar_gastos")
def mostrar_gastos():
    gastos = tracker.mostrar_gastos()
    total= tracker.total_gastos()
    return render_template("mostrar_gastos.html", gastos =gastos, total=total)

@app.route("/informe")
def informe():
    informe_datos = tracker.informe()
    return render_template("informe.html", informe= informe_datos)

if __name__ ==  "__main__":
    app.run(debug=True)