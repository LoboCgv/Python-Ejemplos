from flask import Flask,request
#en request se recibiran los datos

app=Flask(__name__)
@app.route('/addData',methods=["POST","GET"])
#esto significa que las solicitudes que lleguen al servidor con /addData por POST serám recibidos
#por la funcion definida
def addData():
	if(request.is_json):#valida si es un json la solicitud
		content=request.get_json()
		print(content)
		return 'Json Posted';
	else:
		content="no es un formato valido"#en el caso de 
		print(content)
		return content
if __name__=='__main__':
	app.run(debug=True)