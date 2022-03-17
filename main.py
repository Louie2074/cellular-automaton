from flask import Flask, render_template, url_for, request
import cellularAutomaton as ca
app = Flask(__name__)

def parseReq(form):
    rule = 0 if form['rule']== '' else int(form['rule']) 
    rows = 0 if form['rows']== '' else int(form['rows']) 
    col = 0 if form['col']== '' else int(form['col']) 
    style = 0 if form['style']== '' else int(form['style']) 
    lOR = str(form['lOR'])
    return ca.cellular_automaton(rule,rows,col,style,lOR)

@app.route('/', methods=['GET', 'POST'])
def index():
  data = None
  if request.method == 'POST':
    form = request.form
    data = parseReq(form)
    
  return render_template('index.html', data=data)
if __name__ == "__main__":
  app.run(debug=True)
  
