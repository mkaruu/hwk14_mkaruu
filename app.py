from flask import Flask, render_template, request, redirect
from datetime import datetime
import model
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)


def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")


@app.route('/admin')
def admin():
	return render_template('admin.html', entries=model.get_entries())

@app.route('/delete', methods=["POST"])
def delete():
    _id = requests.form["id"]
    model.delete_entry(_id)
    return redirect("/admin")

if __name__ == '__main__':
    model.init()
    app.run(debug=True, use_reloader=True)

