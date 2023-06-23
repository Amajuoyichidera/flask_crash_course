from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# @app.route('/user/<name>')
# def user(name):
#     return f'<h1>Welcome {name}</h1>'

# @app.route('/set')
# def setCookie():
#     response = make_response('cookie set')
#     response.set_cookie('myapp', 'flask web development')

#     return response


# @app.route('/get')
# def getCookie():
#     myapp = request.cookies.get('myapp')
#     return 'cookie content is ' + str(myapp)


if __name__ == '__main__':
    app.run(debug=True)