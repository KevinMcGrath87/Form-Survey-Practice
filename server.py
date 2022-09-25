from flask import Flask, render_template, request, session, redirect,url_for
app = Flask(__name__)
app.secret_key = "deadnuts"


@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/result', methods = ['POST'])
def result():
    session['name']=request.form['name']
    session['dojo']=request.form['dojo']
    session['technique']=request.form['technique']
    session['description']=request.form['description']
    return(redirect('/results'))
    # return(render_template('/result.html'))
@app.route('/results')
def results():
    return(render_template('results.html', name = session['name'], dojo = session['dojo'], technique = session['technique'], description = session['description']))







if __name__== '__main__':
    app.run(debug= True)