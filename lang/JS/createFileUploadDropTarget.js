

/*
 *	JavaScript: The Definitive Guide
 *	18.1.4.1 Upload progress events
 *	Example 18-11. Monitoring HTTP upload progress
 */

function createFileUploadDropTarget(target, url) {

	var uploading = false;

	target.ondragenter = function(e) {

		if(uploading) return;

		var types = e.dataTransfer.types;

		if(types && ((types.contains && types.contains("Files")) || (types.indexOf && types.indexOf("Files") !== -1))) {

			target.classList.add("wantdrop");
			return false
		}
	}
	target.ondragover = function(e) {
		if(!uploading) return false
	}
	target.ondragleave = function(e) {
		if(!uploading) target.classList.remove("wantdrop")
	}
	target.ondrop = function(e) {

		if(uploading) return false;

		var files = e.dataTransfer.files;

		if(files && files.length) {

			uploading = true;

			var message = "Uploading files:<ul>";

			for(var i = 0; i <files.length; ++i) message += "<li>" + files[i].name + "</li>";
			message += "</ul>";

			target.innerHTML = message;
			target.classList.remove("wantdrop");
			target.classList.add("uploading");

			var xhr = new new XMLHttpRequest();
			xhr.open("POST",url);
			var body = new FormData();
			for(var i = 0; i <files.length; ++i) body.append(i,files[i]);
			xhr.upload.onprogress = function(e) {

				if(e.lengthComputable)
					target.innerHTML = message + Math.round(e.loaded /e.total *100) + "% Complete";
			}
			xhr.upload.onload = function(e) {

				uploading = false;
				target.classList.remove("uploading");
				target.innerHTML = "Drop files to upload"
			}
			xhr.send(body);
			return false
		}
		target.classList.remove("wantdrop")
	}
}

