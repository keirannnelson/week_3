import git
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm

app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name

@app.route("/")                          # this tells you the URL the method below is related to
def hello_world():
  return render_template('home.html', subtitle='Home page', text='This is the home page')       # this prints HTML to the webpage
  
@app.route("/second_page")
def second_page():
  return render_template('second_page.html', subtitle='Second Page', text='This is the second page')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)
 
@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/week2/week_3')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")
