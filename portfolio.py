from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Example project data (you can move this to a JSON file later)
projects = [
    {
        "title": "Simple Blog",
        "description": "A minimal blog built with Flask and SQLite.",
        "link": "https://github.com/yourname/simple-blog"
    },
    {
        "title": "Weather App",
        "description": "Shows weather using a public API.",
        "link": "https://github.com/yourname/weather-app"
    }
]

@app.route('/')
def index():
    # render index.html and pass personal info + projects
    return render_template('index.html',
                           name="Your Name",
                           tagline="Python developer | Open-source enthusiast",
                           projects=projects)

@app.route('/project/<int:idx>')
def project_detail(idx):
    try:
        project = projects[idx]
    except IndexError:
        return "Project not found", 404
    return render_template('project.html', project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # get form values
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # ensure a data folder exists and append to a CSV
        os.makedirs('data', exist_ok=True)
        with open('data/contacts.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name, email, message])

        return redirect(url_for('thankyou'))
    return render_template('contact.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
