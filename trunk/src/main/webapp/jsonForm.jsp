<%-- 
    Document   : jsonForm
    Created on : Feb 11, 2009, 10:41:08 AM
    Author     : TwinP
--%>

<%@page contentType="text/html" pageEncoding="windows-1252"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

<html>
    <head>
        <title>
            First Test Spring Json Demo
        </title>
        <script type="text/javascript" src="scripts/prototype.js"></script>
        <script type="text/javascript" src="scripts/behaviour.js"></script>
        <script type="text/javascript" src="scripts/behaviour-roles.js"></script>
        <meta content="text/html; charset=ISO-8859-1" http-equiv="Content-Type"/>
    </head>
    </head>
<body>
	<h1>Spring-Json Demo</h1>
	<p> The following examples demonstrate Spring-Json in action. The  returned Json objects are displayed in alert() dialogs before
	being inserted into the document. </p>

	<h2>1. Ajax Get (ControllerInterface)</h2>

	<p>Clicking the 'Get Name' button gets a Json object from 'hello.json'.
	The 'Clear Name' button simply replaces the existing text with empty strings</p>
	<fieldset>
		<legend>Returned values</legend>
		<label for='firstname' >First Name : </label><span id="firstname"></span><br/>
		<label for='secondname' >Surname : </label><span id="secondname"></span><br/>
		<button id="clearName" class="floated-right">Clear Name</button>
	</fieldset>
	<div class="wrapper">
	<button id="getName" class="centred">Get Name</button>
	</div>
	<h2>2. Ajax Post</h2>

	<p>In this example the values entered on the form are POSTed to the server and then returned in a Json object which is used to update the 'returned values' below</p>
	<form method="post" id="form">
	<fieldset>
		<legend>Form values</legend>
		<label for="placeofbirth">Place of Birth</label><input id="placeofbirth" type="text" name="placeofbirth" ><br>
		<label for="birthday">Date of Birth</label><input id="birthday" type="text" name="birthday" ><br/>
		<button id="clearData" class="floated-right">Clear Form Values</button>
	</fieldset>
	</form>
	<div >
	<button id="sfc_postData" class="big-button">Send data to SimpleFormController</button>
	<button id="cc_postData" class="big-button">Send data to CommandController</button>
	<p> The following buttons demonstrate the use of ConfiguratorTemplates to exclude properties</p>
	<button id="sfc_postData_sojo2" class="big-button">Using SojoJsonWriterConfiguratorTemplate to exclude 'Place of birth' property)</button>
	<button id="sfc_postData_jsonlib" class="big-button">Using JsonlibJsonWriterConfiguratorTemplate to exclude 'Date of Birth' property)</button>
	</div>
	<fieldset>
		<legend>Returned values</legend>
		<label for="t_placeofbirth">Place of Birth : </label><span id="t_placeofbirth"></span><br/>
		<label for="t_birthday">Date of Birth : </label><span id="t_birthday"></span><br/>

	</fieldset>
	<p id ="error" ></p>

	<h2>3. Exception-Handling by JsonExceptionResolver</h2>
	<p>Hopefully you have not encountered an error so far...</p>
	<div class="wrapper">
	<button id="throwException">Throw an exception</button>
	</div>
</body>
</html>
