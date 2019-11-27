// alek westover
// node terrible hacks
// grab the packages we need
var express = require('express');
var app = express();
var port = process.env.PORT || 3000;

// routes will go here

// start the server
app.listen(port);
console.log('Server started! At http://localhost:' + port);

app.use(express.static('public'));

var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies


// POST http://localhost:8080/api/users
// parameters sent with 
app.post('/', function(req, res) {
    var user_id = req.body.id;
    var token = req.body.token;
    var geo = req.body.geo + "POST";
    res.redirect("output.html?"+user_id);
});


function joinIns(ins, fields)
{
	var out = "";
	if (ins.length<1)
	{
		return out;
	}
	for (var i = 0; i < ins.length-1; i++)
	{	
		out+=ins[i]+"="+fields[i]+"&";
	}
	out+= ins[ins.length-1]+"="+fields[ins.length-1];
	return out;
}

function parseURL(url)
{
	var lastPart = url.split("?");
	lastPart = lastPart[lastPart.length-1];
	var terms = lastPart.split("&");
	var data = {};
	for (var t = 0; t < terms.length; t++)
	{
		var curt = terms[t].split("=");
		data[curt[0]] = curt[1];
	}
	return data;
}
