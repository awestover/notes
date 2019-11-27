// grab the packages we need
var express = require('express');
var app = express();
var port = process.env.PORT || 8080;

// routes will go here

// start the server
app.listen(port);
console.log('Server started! At http://localhost:' + port);

app.use(express.static('public'));

// routes will go here
app.get('/output.html', function(req, res) {
  var user_id = req.param('id');
  var token = req.param('token');
  var geo = req.param('geo')+"chicken";  

  res.send(user_id + ' ' + token + ' ' + geo);
});

// parameter middleware that will run before the next routes
// app.param('name', function(req, res, next, name) {

//     // check if the user with that name exists
//     // do some validations
//     // add -dude to the name
//     var modified = name + '-dude';

//     // save name to the request
//     req.name = modified;

//     next();
// });

// http://localhost:8080/chris
// app.get('/:name', function(req, res) {
//   // the user was found and is available in req.user
//   res.send('What is up ' + req.name + '!');
// });

var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies


// POST http://localhost:8080/api/users
// parameters sent with 
app.post('/output.html', function(req, res) {
    var user_id = req.body.id;
    var token = req.body.token;
    var geo = req.body.geo + "POST";

    res.send(user_id + ' ' + token + ' ' + geo);
});
