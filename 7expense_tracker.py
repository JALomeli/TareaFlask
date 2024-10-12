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
        self.presupuesto=0

    def agregar_gasto(self, categoria: str, monto: float):
        gasto = Gasto(categoria, monto)
        self.lista.append(gasto)
        flash(f"Gasto agregado con exito :) , Categoria: {categoria} | Monto: ${monto}")
        if self.exceso_presupuesto():
            flash("Se excedio tu presupuesto CUIDADITO!")

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

    def establecer_presupuesto(self, monto:float):
        self.presupuesto = monto
        flash(f"Presupuesto: ${monto}")

    def exceso_presupuesto(self):
        total_gastos =self.total_gastos()
        return total_gastos > self.presupuesto
tracker = Expense_tracker()

@app.route("/")
def index():
    return render_template("inicio.html", presupuesto=tracker.presupuesto)

@app.route("/establecer_presupuesto", methods=["GET", "POST"])
def establecer_presupuesto():
    if request.method== "POST":
        presupuesto = float(request.form["presupuesto"])
        tracker.establecer_presupuesto(presupuesto)
        return redirect(url_for("index"))
    return render_template("establecer_presupuesto.html")


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
    presupuesto_excedido = tracker.exceso_presupuesto()
    return render_template("mostrar_gastos.html", gastos =gastos, total=total, presupuesto_excedido = presupuesto_excedido)

@app.route("/informe")
def informe():
    informe_datos = tracker.informe()
    return render_template("informe.html", informe= informe_datos)

if __name__ ==  "__main__":
    app.run(debug=True)