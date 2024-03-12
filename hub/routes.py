from hub import app,render_template,blu


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@blu.route('/shop')
def shop():
    return render_template('e commerce.html')


app.register_blueprint(blu, url_prefix='/ai')