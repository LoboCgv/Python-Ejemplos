<script type="text/javascript">
  function actualizar(){
	  location.reload(true);//regarca la pagina
	 
	  }
  setInterval("actualizar()",5000);//los datos serán enviados cada 5 segundos
</script>

<?PHP
$fecha=date("d/m/y:h:i:s");
$url="localhost:5000/addData";//direccion de envio 
$data=array("deviceid"=>1,"lat"=>-34.9866,"lng"=>-70.6454,"tiempo"=>$fecha);//datos a enviar
$content = json_encode($data);
$curl = curl_init($url);//es importante mantener instalado curl
curl_setopt($curl, CURLOPT_HEADER, false);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_HTTPHEADER,
        array("Content-type: application/json"));
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_POSTFIELDS, $content);
$json_response = curl_exec($curl);
$status = curl_getinfo($curl, CURLINFO_HTTP_CODE);
if ( $status != 200 ) {
    die("Error: call to URL $url failed with status $status, response $json_response, curl_error " . curl_error($curl) . ", curl_errno " . curl_errno($curl));
}
curl_close($curl);
$response = json_decode($json_response, true);
?>
