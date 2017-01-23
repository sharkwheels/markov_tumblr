#################################
# Markov Search | APP End
# Nadine Lessio 2016 Winter
# IAMD_RI
# V1.0
# This is the front end so there's a web presence
##################################

### IMPORTS ####################################################################

from flask import Flask, render_template, request, redirect, url_for, flash

### FLASK SETUP  ####################################################################
app = Flask(__name__, static_folder='static',static_url_path='/static')
app.config['DEBUG'] = True
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

### APP VIEWS ####################################################################

@app.route("/",methods=['GET','POST'])

def main():
	return render_template('main.html')
	

### RUN IT ####################################################################

if __name__ == '__main__': # If we're executing this app from the command line
    #app.run("127.0.0.1", port = 3000, debug=True, use_reloader=True)
    app.run(debug=False, use_reloader=False)
