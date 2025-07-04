

if(!Function.prototype.bind) {
	Function.prototype.bind = function(o) {

		var self = this;
		var outer = arguments;

		return function() {

			var args = [];
			var i;

			for(i = 1; i <outer.length; ++i) args.push(outer[i]);
			for(i = 0; i <arguments.length; ++i) args.push(arguments[i]);

			return self.apply(o,args)
		}
	}
}

