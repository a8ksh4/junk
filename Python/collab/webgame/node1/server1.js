var http = require('http');
var mongo = require('mongodb'), Server = mongo.Server, Db = mongo.Db;
var Connection = mongo.Connection;

console.log("starting to run");

http.createServer(function(request, response) {
    var server = new Server('localhost', Connection.DEFAULT_PORT, {});
    var db = new Db('webgamedb', server);
    
    console.log("web hit");
    db.open(function(err, db) {
	if(!err) {
	    response.writeHead(200, {"Content-Type": "text/plain"});
	    db.collection('ships', function(err, collection) {
		collection.find().toArray(function(err, items) {
		    response.write(JSON.stringify(items));
		    response.end();
		});
	    });
	}
    });
}).listen(8888);
