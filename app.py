from flask import Flask,render_template
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name="NEHA HG"
    username=os.getlogin()
    ist=pytz.timezone('Asia/Bangalore')
    server_time=datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    try:
        top_output=subprocess.check_output(['top','-b','-n','1']).decode('utf-8')
    except Exception as e:
        top_output=f"Error running 'top':{e}"
    return render_template('index.html',full_name=full_name,username=username,server_time=server_time,top_output=top_output)
    if __name__=='__main__':
        app.run(host='0.0.0.0',port=5000)


