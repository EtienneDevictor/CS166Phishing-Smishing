from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def results():
    p_count = clicks('./phishing.txt')
    s_count = clicks('./smishing.txt')
    return f'Phishing Clicks: {p_count}, Smishing Clicks: {s_count}'

@app.route('/Phishing/<id>')
def phishing(id):
    findOrAppend(f'./phishing.txt', id)
    return redirect('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')
    
@app.route('/Smishing/<id>')
def smishing(id):
    findOrAppend('./smishing.txt', id)
    return redirect("https://www.ups.com/track?loc=en_US&requester=ST/")
    

def findOrAppend(filename, id):
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        if line.strip() == id:
            return
    file.close()
    file = open(filename, "a")
    file.write(f'{id}\n')
    file.close()
    
def clicks(filename):
    file = open(filename, "r")
    lines = file.readlines()
    count = 0
    for line in lines:
        count += 1
    
    return count
    
        

if __name__ == '__main__':
   app.run(debug = True)