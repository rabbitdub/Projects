from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == 'POST':
        password = request.form["inputPass"]
        name_from_form = request.form["inputName"]
        tortilla = request.form["tortilla"]
        rice = request.form["Rice"]
        beans = request.form["beans"]
        protein = request.form["protein"]
        add_ingred = request.form.getlist("check")
        deliv_instruct = request.form["delivIn"]
        print(deliv_instruct)
        print(add_ingred)
        print(protein)
        print(beans)
        print(rice)
        print(tortilla)
        print(password)
        print(name_from_form)
        return render_template("home.html", name_from_form = name_from_form, password = password, tortilla = tortilla, rice = rice, beans = beans, protein = protein, add_ingred = add_ingred, deliv_instruct = deliv_instruct)
   
   

app.run(debug=True)