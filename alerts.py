from flask import Flask, request, render_template  
  
# Flask constructor 
app = Flask(__name__)    
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/getdata', methods =["GET", "POST"]) 
def gfg(): 
     edgeId = request.body.edgeId
     dpName = request.body.DP
     alertName = request.body.alertName
     reviewP = request.body.rP
     number = request.body.number
     thresh = request.body.thresh
     alert = request.body.alert
     operator = request.body.operator

   
    
        doc = {
            edgeId : edgeId,
            dpName : dpName,
            alertName : alertName,
            reviewP : reviewP,
            number : number,
            thresh : thresh,
            alert : alert,
            operator : operator
        }

    if request.method == "POST": 
       print doc
    return render_template("form.html") 
  
if __name__=='__main__': 
   app.run() 


 

 def contact1(): 
   # this line goes to the console/terminal in flask dev server
    print (request.form)
    # this line prints out the form to the browser
    return jsonify(request.form.to_dict())
