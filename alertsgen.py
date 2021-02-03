from flask import Flask, render_template, request, flash, jsonify
from forms import ContactForm
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods = ['GET'])
def index():
   return 'this is Alert Form Application'

 
@app.route('/getform/', methods = ['GET','POST'])
            
def contact():
   
   form = ContactForm()
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         print (request.args)
         return jsonify(request.form.to_dict())
      else:
         return render_template('success.html')     
   elif request.method == 'GET':
        return render_template('contact.html', form = form)

      

if __name__ == '__main__':
   app.run(debug = True)