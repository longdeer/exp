

exports.get = function(url, callback) {

	url = require("url").parse(url);

	var host = url.hostname;
	var port = url.port || 54321;
	var path = url.pathname;
	var query = url.query;

	if(query) path += `?${query}`;

	var client = require("http").createClient(port,host);
	var request = client.request("GET", path,{ "Host": host });

	request.end();

	request.on(

		"response",
		res => {

			res.setEncoding("utf8");

			var body = "";

			res.on("data",chunk => body += chunk);
			res.on("end",callback => callback(res.statusCode, res.headers, body))
		}
	)
}


exports.post = function(url, data, callback) {

	url = require("url").parse(url);

	var host = url.hostname;
	var port = url.port || 54321;
	var path = url.pathname;
	var query = url.query;
	var type;

	if(query) path += `?${query}`;
	if(data == null) data = "";
	if(data instanceof Buffer) type = "application/octet-stream";
	else
	if(typeof data === "string") type = "text/plain; charset=UTF-8";
	else
	if(typeof data === "object") {

		data = require("querystring").stringify(data);
		type = "application/x-www-form-urlencoded";
	}
	var client = require("http").createClient(port,host);
	var request = client.request("POST", path,{ "HOST": host, "Content-Type": type });

	request.write(data);
	request.end();
	request.on(

		"response",
		res => {

			res.setEncoding("utf8");

			var body = "";

			res.on("data",chunk => body += chunk);
			res.on("end",callback => callback(res.statusCode, res.headers, body))
		}
	)
}

