from flask import Flask, render_template, request, redirect, url_for, flash

app=Flask(__name__)
app.secret_key="llavesupersecreta"

class Account:
    def __init__(self, name, initial_balance):
        self.name= name
        self.balance = initial_balance
        self.transactions=[f"Cuenta creada con saldo inical de {initial_balance}"]
    
    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f"Depósito: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount and amount > 0:
            self.balance -= amount
            self.transactions.append(f"Retiro: {amount}")  
        else:
            flash(f"Fondos insuficientes o cantidad inválida en la cuenta de {self.name}")
            
    def check_balance(self):
        return self.balance
        
    def generate_statement(self):
        flash(f"\nEstado de cuenta de {self.name}")
        for transaction in self.transactions:
            flash(transaction)
        self.check_balance()
        
class Bank:
    def __init__(self):
        self.accounts={}
    
    def create_account(self, name, initial_balance):
        if name in self.accounts:
            flash("La cuenta ya existe")
        else:
            self.accounts[name] = Account(name, initial_balance)
            flash(f"Cuenta creadad para {name} con saldo inicial ed {initial_balance}")
        
    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account].balance >= amount and  amount > 0:
                self.accounts[from_account].withdraw(amount)
                self.accounts[to_account].deposit(amount)
                flash(f"Se ha transferido {amount} de {from_account} a {to_account}.")
            else:
                flash("Fondos inuficientes en lla cuenta de origen")
        else:
            flash("Una o ambas cuentas no existen")

bank=Bank()

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method== "POST":
        account= request.form["account"]
        amount= float(request.form["initial_balance"])
        if account in bank.accounts:
            flash(f"La cuenta ya existe")
        else:
            bank.create_account(account, amount)
        return redirect(url_for("index"))
    return render_template("create_account.html")

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method== "POST":
        account= request.form["account"]
        amount= float(request.form["amount"])
        if account in bank.accounts:
            bank.accounts[account].deposit(amount)
            flash(f"Se ha depositado {amount} en la cuenta de {account}")
        else:
            flash("La cuenta no existe")
        return redirect(url_for("index"))
    return render_template("deposit.html")

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method=="POST":
        account= request.form["account"]
        amount= float(request.form["amount"])
        if account in bank.accounts:
            bank.accounts[account].withdraw(amount)
        else:
            flash("La cuenta no existe")
        return redirect(url_for("index"))
    return render_template("withdraw.html")

@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    if request.method== "POST":
        from_account = request.form["from_account"]
        to_account = request.form["to_account"]
        amount= float(request.form["amount"])
        if from_account in bank.accounts and to_account in bank.accounts:
            bank.transfer(from_account, to_account,amount)
        return redirect(url_for("index"))
    return render_template("transfer.html")


@app.route("/check_balance", methods=["GET", "POST"])
def check_balance():
    if request.method== "POST":
       account = request.form["account"]
       if account in bank.accounts:
            balance = bank.accounts[account].check_balance()
            flash(f"El saldo de {account} es: {balance}")
       else:
            flash("La cuenta no existe")
       return redirect(url_for("index"))
    return render_template("check_balance.html")

@app.route("/generate_statement", methods=["GET", "POST"])
def generate_statement():
    if request.method== "POST":
       account = request.form["account"]
       if account in bank.accounts:
            transactions = bank.accounts[account].generate_statement()
            return render_template("statement.html", transactions= transactions, account=account)
       else:
            flash("La cuenta no existe")
       return redirect(url_for("index"))
    return render_template("generate_statement.html")

if __name__=="__main__":
    app.run(debug=True)