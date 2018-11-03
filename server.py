from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)

    strawberry = request.form['strawberry']
    blackberry = request.form['blackberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    firstName = request.form['first_name']
    lastname = request.form['last_name']
    email = request.form['student_id']
    total = int(strawberry) + int(blackberry) + int(raspberry) + int(apple)

    return render_template("checkout.html", 
    s = strawberry, b = blackberry, r = raspberry, a = apple,
    first = firstName, last = lastname, id = email, t = total)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    