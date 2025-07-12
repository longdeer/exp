

var http = require("http");
var fs = require("fs");
var url;

var server = new http.Server();
server.listen(54321);

server.on(

	"request",
	(req,res) => {

		url = require("url").parse(req.url)

		if(url.pathname === "/test/delay") {

			var delay = parseInt(url.query) || 2000;

			res.writeHead(200,{ "Content-type": "text/plain; charset=UTF-8" });
			res.write(`sleeping for ${delay} milliseconds`);

			setTimeout(() => { res.write("done."); res.end() }, delay)
		}
		else
		if(url.pathname === "/test/mirror") {

			res.writeHead(200,{ "Content-type": "text/plain; charset=UTF-8" });
			res.write(`${req.method} ${req.url} HTTP/${req.httpVersion}\r\n`);

			for(var h in req.headers) res.write(`${h}: ${req.headers[h]}\r\n`);
			res.write("\r\n");

			req.on("data",chunk => res.write(chunk));
			req.on("end",() => res.end())
		}
		else {

			var fileName = url.pathname.sustring(1);
			var type;

			switch(fileName.substring(fileName.lastIndexOf(".") +1)) {

				case "htm":
				case "html":	 type = "text/html; charset=UTF-8"; break;
				case "js":		 type = "application/javascript; charset=UTF-8"; break;
				case "css":		 type = "text/css; charset=UTF-8"; break;
				case "txt":		 type = "text/plain; charset=UTF-8"; break;
				case "manifest": type = "text/cache-manifest; charset=UTF-8"; break;
				default:		 type = "application/octet-stream"; break;
			}
			fs.readFile(

				fileName,
				(err,content) => {

					if(err) {

						res.writeHead(404,{ "Content-type": "text/plain; charset=UTF-8" });
						res.write(err.message);
						res.end();
					}
					else {

						res.writeHead(200,{ "Content-type": type });
						res.write(content);
						res.end()
					}
				}
			)
		}
	}
)

