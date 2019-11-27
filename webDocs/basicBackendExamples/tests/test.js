var parse = require('querystring').parse;
var http = require('http');
console.log("started server");
var server = http.createServer((req, res) => {
	if (req.method === 'POST') {
        // Handle post info...
        var body = '';
	    req.on('data', chunk => {
	        body += chunk.toString(); // convert Buffer to string
	    });
	    req.on('end', () => {
	        var pb = parse(body);
	        var resp = "";
	        for (var i in pb)
	        {
	        	resp += i + ": " + pb[i]+ "\n"
	        }
	        res.end(resp);
	    });
    }
    else {
	    res.end(`
	        <!doctype html>
	        <html>
	        <body>
	            <form action="/" method="post">
	                <input type="text" name="fname" /><br />
	                <input type="text" name="kname" /><br />
	                <button>Save</button>
	            </form>
	        </body>
	        </html>
	    `);
	}
});
server.listen(3000);

