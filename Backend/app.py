from flask import Flask, jsonify

from flask_cors import CORS



app = Flask(__name__)
CORS(app) 

# Sample data
data = [
    {"name": "max mustermann", "email": "max_mustermann@example.com", "birthdate": "1990-09-01"},
    {"name": "Jane Smith", "email": "jane@example.com", "birthdate": "1985-05-15"},
    {"name": "John mustermann", "email": "John_mustermann@example.com", "birthdate": "2010-12-15"},
    {"name": "Jason nicolas", "email": "Jason_nicolasn@example.com", "birthdate": "2004-12-15"},
    {"name": "Sophia Miller", "email": "sophia.miller@example.com", "birthdate": "1992-04-20"},
    {"name": "Liam Johnson", "email": "liam.johnson@example.com", "birthdate": "1987-11-10"},
    {"name": "Olivia Brown", "email": "olivia.brown@example.com", "birthdate": "2001-07-05"},
    {"name": "Noah Davis", "email": "noah.davis@example.com", "birthdate": "2015-02-18"},
    {"name": "Emma Wilson", "email": "emma.wilson@example.com", "birthdate": "1976-09-30"},
    {"name": "William Taylor", "email": "william.taylor@example.com", "birthdate": "1998-12-25"},
    {"name": "Ava Martinez", "email": "ava.martinez@example.com", "birthdate": "1984-03-12"},
    {"name": "James Anderson", "email": "james.anderson@example.com", "birthdate": "2005-06-08"},
    {"name": "Isabella Thomas", "email": "isabella.thomas@example.com", "birthdate": "1990-10-03"},
    {"name": "Oliver Garcia", "email": "oliver.garcia@example.com", "birthdate": "2012-01-29"},
    {"name": "Charlotte Rodriguez", "email": "charlotte.rodriguez@example.com", "birthdate": "1989-08-14"},
    {"name": "Elijah Martinez", "email": "elijah.martinez@example.com", "birthdate": "2000-03-27"},
    {"name": "Amelia Lee", "email": "amelia.lee@example.com", "birthdate": "1975-12-08"},
    {"name": "Benjamin White", "email": "benjamin.white@example.com", "birthdate": "1996-05-22"},
    {"name": "Mia Hernandez", "email": "mia.hernandez@example.com", "birthdate": "2010-10-01"},
    {"name": "Ethan Thompson", "email": "ethan.thompson@example.com", "birthdate": "1982-11-05"},
    {"name": "Harper Moore", "email": "harper.moore@example.com", "birthdate": "1993-07-19"},
    {"name": "Lucas Hall", "email": "lucas.hall@example.com", "birthdate": "2008-02-13"},
    {"name": "Amelia Allen", "email": "amelia.allen@example.com", "birthdate": "1997-09-26"},
    {"name": "Avery Perez", "email": "avery.perez@example.com", "birthdate": "2003-04-30"},
    {"name": "Evelyn Scott", "email": "evelyn.scott@example.com", "birthdate": "1987-01-17"},
    {"name": "Logan Carter", "email": "logan.carter@example.com", "birthdate": "2014-06-24"},
    {"name": "Aria Nguyen", "email": "aria.nguyen@example.com", "birthdate": "2006-09-09"},
    {"name": "Sebastian Hill", "email": "sebastian.hill@example.com", "birthdate": "1980-08-03"},
    {"name": "Grace Baker", "email": "grace.baker@example.com", "birthdate": "1995-03-11"},
    {"name": "Mason Mitchell", "email": "mason.mitchell@example.com", "birthdate": "2002-12-07"},
    {"name": "Isabella Lopez", "email": "isabella.lopez@example.com", "birthdate": "2011-05-28"},
    {"name": "Jackson Adams", "email": "jackson.adams@example.com", "birthdate": "1978-10-16"},
    {"name": "Sophie Turner", "email": "sophie.turner@example.com", "birthdate": "1994-11-02"},
    {"name": "Daniel Parker", "email": "daniel.parker@example.com", "birthdate": "2009-07-23"}
]

@app.route('/', methods=['GET'])
def get_table():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)