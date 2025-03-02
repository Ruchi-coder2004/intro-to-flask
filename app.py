from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Coder',        
        'location': 'Bengaluru, India',
        'salary': 'Rs. 1,00,000'
    },
    {
        'id': 2,
        'title': 'Developer',        
        'location': 'Delhi, India',
        'salary': 'Rs. 1,50,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',        
        'location': 'Remote',
        'salary': 'Rs. 1,20,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',        
        'location': 'San Francisco, USA',
        'salary': '1,50,000'
    },
    {
        'id': 5,
        'title': 'Software Engineer',        
        'location': 'San Francisco, USA',
        'salary': '2,00,000'
    }
]


@app.route('/')
def home():
    return render_template('home.html',jobs=JOBS,company_name='Just For Learn')

@app.route('/api/jobs')
def list_jobs():
    return josinify(JOBS)

if __name__ == '__main__':
    print("Starting app...")
    app.run(debug=True,host="0.0.0.0", port=5000)
