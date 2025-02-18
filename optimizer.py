from models import db, MeetingAvailability
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

def find_best_meeting_time():
    all__entries = MeetingAvailability.query.all()
    time_slots = list(set([entry.time_slot for entry in all__entries]))
    
    # Mapping time slots to indices as user
    user_availability = {}
    for entry in all__entries:
        if entry.user not in user_availability:
            user_availability[entry.user] = []
        user_availability[entry.user].append(entry.time_slot)
    
    # create problem
    model = LpProblem("Meeting_Scheduler", LpMaximize)
    x = {t: LpVariable(name=f"time_{t}", cat="Binary") for t in time_slots}
    
    # objective function
    model += lpSum(x[t] for t in time_slots)
    
    # constraints
    for user, times in user_availability.items():
        model += lpSum(x[t] for t in times) >= 1

    model.solve()
    
    best_time = [t for t in time_slots if x[t].value() == 1]
    return {"best_time": best_time}
