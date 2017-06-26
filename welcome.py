# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/IBMDomainVerification.html')
def asoc():
    return app.send_static_file('IBMDomainVerification.html')

@app.route('/terms')
def terms():
    return app.send_static_file('terms.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'Kevin Rothman', 'job': 'Principal'},
        {'name': 'Cliff Archey', 'job' : 'IBM Liason'},
        {'name': 'Eric Waliskewski', 'job' : 'Math Teacher'},
        {'name': 'Dan Svarczkopf', 'job' : 'CS Teacher'},
        {'name': 'Jackie Hessee', 'job' : 'ELA Teacher'},
        {'name': 'Mary Amante-Gordon', 'job' : 'Math Teacher'},
        {'name': 'Torrance Harvey', 'job' : 'History Teacher'},
        {'name': 'Christine McCartney', 'job' : 'ELA Teacher'},
        {'name': 'Joyce DImperio', 'job' : 'Science Teacher'}
        ];
    return jsonify(results=list)

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
