from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from models import db, MeetingAvailability
from optimizer import find_best_meeting_time
import os


app = Flask(__name__)
CORS(app)

# dev version
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meetings.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#vercel version
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///meetings.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_availability():
    data = request.json
    user = data['user']
    available_times = data['available_times']

    for time in available_times:
        new_entry = MeetingAvailability(user=user, time_slot=time)
        db.session.add(new_entry)

    db.session.commit()
    return jsonify({"message": "Availability saved!"})

@app.route('/optimize', methods=['POST'])
def optimize_meeting():
    data = request.json
    users = data['users']

    # solve the problem
    common_times = set(users[next(iter(users))])
    for user, times in users.items():
        common_times.intersection_update(times)

    return jsonify({"best_time": list(common_times)})


# Vercel version
def handler(event, context):
    return app(event, context)


# # Local version
# if __name__ == '__main__':
#     app.run(debug=False)
