from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user(): 
    name = request.form['name']
    dojo = request.form['dojo']
    language = request.form['language']
    comment = request.form['comment']
    print(request.form)
    return render_template('success.html', name=name, dojo=dojo, language=language, comment=comment)
    
@app.route('/danger')
def danger():
    print("A user tried to visit /danger. We have directed the user to /")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)