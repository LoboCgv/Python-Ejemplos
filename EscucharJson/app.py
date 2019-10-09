from flask import Flask,request
#en request se recibiran los datos
import mysql.connector
app=Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  port="3306",
  #si conocemos la base de datos ponemos aca
  database="flask_coordenadas"
)

@app.route('/addData',methods=["POST","GET"])
#esto significa que las solicitudes que lleguen al servidor con /addData por POST serám recibidos
#por la funcion definida
def addData():
	if(request.is_json):#valida si es un json la solicitud
		content=request.get_json()
		cursor=mydb.cursor()
		consulta="insert into devicepos (deviceId,lat,lng,fecha) values ("+str(content["deviceid"])+","+str(content["lat"])+","+str(content["lng"])+",'"+str(content["tiempo"])+"')"
		cursor.execute(consulta)
		mydb.commit()
		print(content)#mantengo el print sólo para tener un registro en la ventana
		return 'Json Posted';
	else:
		content="no es un formato valido"#en el caso de 
		print(content)
		return content
if __name__=='__main__':
	app.run(debug=True)