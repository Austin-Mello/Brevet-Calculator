<html>
    <head>
	<meta charset="utf-8">
        <title>Brevet Times Calculator-api demo</title>
    </head>

    <body>

<?php
if(array_key_exists('ListAll', $_POST)){
	$URI = "";
	if(!empty($_POST['JSON']) and !empty($_POST['CSV'])){
		echo 'YOU FOOL! I TOLD YOU NOT TO DO IT! YOU HAVE DOOMED US ALL!';
	}
	else if(!empty($_POST['JSON'])){
		$URI = '/json';
		listAll($URI);
	}	
	else if(!empty($_POST['CSV'])){
		$URI = '/csv';
		listAll($URI);
	}
	else {
		listAll($URI);
	}
}

if(array_key_exists('ListOpenOnly', $_POST)){
	$top = $_POST['topo'];
	if ($top > 0){
		$top = "?top=" . $top;
	}
	//$URI = "";
	if(!empty($_POST['JSONo']) and !empty($_POST['CSVo'])){
		echo 'YOU FOOL! I TOLD YOU NOT TO DO IT! YOU HAVE DOOMED US ALL!';
	}
	else if(!empty($_POST['JSONo'])){
		$URI = '/json';
		listOpen($URI, $top);
	}	
	else if(!empty($_POST['CSVo'])){
		$URI = '/csv';
		listOpen($URI, $top);
	}
	else {
		listOpen($URI, $top);
	}
}

if(array_key_exists('ListClosedOnly', $_POST)){
	$top = $_POST['topc'];
	if ($top > 0){
		$top = "?top=" . $top;
	}
	//$URI = "";
	if(!empty($_POST['JSONc']) and !empty($_POST['CSVc'])){
		echo 'YOU FOOL! I TOLD YOU NOT TO DO IT! YOU HAVE DOOMED US ALL!';
	}
	else if(!empty($_POST['JSONc'])){
		$URI = '/json';
		listClose($URI, $top);
	}	
	else if(!empty($_POST['CSVc'])){
		$URI = '/csv';
		listClose($URI, $top);
	}
	else {
		listClose($URI, $top);
	}
}

function listAll($tail){
	switch ($tail){
		case '/json':
			echo "routing to json";
			$listAll_url = 'http://calculator:5000/listAll' . $tail;
			$json = file_get_contents($listAll_url);
			$obj = json_decode($json);
	  		$Brevets = $obj->dict;
    				foreach ($Brevets as $l) {
					foreach($l as $i) {
						echo "<li>$i</li>";
					}
				}
			break;	
		case '/csv':
			echo 'routing to csv';
			$listAll_url = 'http://calculator:5000/listAll' . $tail;
			$csv = file_get_contents($listAll_url);
			echo "<li>$csv</li>";
			break;
		default:
			echo "routing to default";
			$listAll_url = 'http://calculator:5000/listAll';
			$json = file_get_contents($listAll_url);
			$obj = json_decode($json);
	  		$Brevets = $obj->dict;
    				foreach ($Brevets as $l) {
					foreach($l as $i) {
						echo "<li>$i</li>";
					}	
				}
			break;
	}
}

function listOpen($tail, $top){
	switch ($tail){
		case '/json':
			echo "routing to json";
			$listOpen_url = 'http://calculator:5000/listOpenOnly' . $tail . $top;
			$json = file_get_contents($listOpen_url);
			$obj = json_decode($json);
	  		$Brevets = $obj->dict;
			foreach ($Brevets as $l) {
				if (is_array($l)){
					foreach($l as $i) {
						echo "<li>$i</li>";
					}
				}
				else {echo "<li>$l</li>";}
			}
			break;	
		case '/csv':
			echo 'routing to csv';
			$listOpen_url = 'http://calculator:5000/listOpenOnly' . $tail . $top;
			$csv = file_get_contents($listOpen_url);
			echo "<li>$csv</li>";
			break;
		default:
			echo "routing to default";
			$listOpen_url = 'http://calculator:5000/listOpenOnly'. $top;
			$json = file_get_contents($listOpen_url);
			$obj = json_decode($json);
	  		$Brevets = $obj->dict;
			foreach ($Brevets as $l) {
				if (is_array($l)){
					foreach($l as $i) {
						echo "<li>$i</li>";
					}
				}
				else {echo "<li>$l</li>";}
			}
			break;
	}
}

function listClose($tail, $top){
	switch ($tail){
		case '/json':
			echo "routing to json";
			$listClose_url = 'http://calculator:5000/listCloseOnly' . $tail . $top;
			$json = file_get_contents($listClose_url);
			$obj = json_decode($json);
	  		$Brevets = $obj->dict;
			foreach ($Brevets as $l) {
				if (is_array($l)){
					foreach($l as $i) {
						echo "<li>$i</li>";
					}
				}
				else {echo "<li>$l</li>";}
			}
			break;	
		case '/csv':
			echo 'routing to csv';
			$listClose_url = 'http://calculator:5000/listCloseOnly' . $tail . $top;
			$csv = file_get_contents($listClose_url);
			echo "<li>$csv</li>";
			break;
		default:
			echo "routing to default";
			$listClose_url = 'http://calculator:5000/listCloseOnly'. $top;
			$json = file_get_contents($listClose_url);
			$obj = json_decode($json);
	  		$Brevets = $obj->dict;
			foreach ($Brevets as $l) {
				if (is_array($l)){
					foreach($l as $i) {
						echo "<li>$i</li>";
					}
				}
				else {echo "<li>$l</li>";}
			}
			break;
	}
}

?>

      <form  method="post", name='listAll'>
	<input type='submit'name='ListAll' class='button' value='List All'/>
	<input type='radio' name='JSON' value='JSON'/>JSON
	<input type='radio' name='CSV'value='CSV'/>CSV<br>
	Leave checkboxes blank for just /listAll<br>
	Check em to append JSON or CSV<br>
	Don't check them both together, or the universe will be destroyed.
      </form>
 
      <form  method="post", name='listOpen'>
	<input type='number' name='topo'/>
	<input type='submit'name='ListOpenOnly' class='button' value='List Open'/>
	<input type='radio' name='JSONo' value='JSON'/>JSON
	<input type='radio' name='CSVo'value='CSV'/>CSV<br>
	Type a number into the box for ?top=k <br>
	Leave checkboxes blank for just /listOpen<br>
	Don't check them both together, or the universe will be destroyed.
      </form>
      <form  method="post", name='listClose'>
	<input type='number' name='topc'/>
	<input type='submit'name='ListClosedOnly' class='button' value='List Close'/>
	<input type='radio' name='JSONc' value='JSON'/>JSON
	<input type='radio' name='CSVc'value='CSV'/>CSV<br>
	Type a number into the box for ?top=k <br>
	Leave checkboxes blank for just /listClose<br>
	Don't check them both together, or the universe will be destroyed.
      </form>
    </body>
</html>
