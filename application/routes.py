from flask import render_template
from application import app

dummyData = [
{
"name": {"first":"Chester", "last":"Gardner"},
"title":"First Post",
"content":"This is some dummy data for Flask lectures"
},
{
"name": {"first":"Chris", "last":"Perrins"},
"title":"Second Post",
"content":"This is even more dummy data for Flask lectures"
}
]



@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home', posts=dummyData)
