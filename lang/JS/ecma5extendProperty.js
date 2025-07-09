

Object.defineProperty(

	Object.prototype,
	"extend",
	{
		writable: true,
		enumerable: false,
		configurable: true,
		value: function extend() {

			var i;
			var j;
			var src;
			var names;

			/*
				The first part is a standard behaviour for environments other than IE,
				which is known to have a certain bug for properties enumeration.
			*/
			for(var p in { toString: null })
				for(i = 0; i <arguments.length; ++i) {

					src = arguments[i];
					names = Object.getOwnPropertyNames(src);

					for(j = 0; j <names.length; ++j)
						Object.defineProperty(this, names[j], Object.getOwnPropertyDescriptor(src,names[j]))
				}
				return;

			/*
				This point means it is IE environment, so the bug when for/in loop
				won't enumerate an enumerable property of "o" if the prototype of "o"
				has a nonenumerable property by the same name.
			*/
			for(i = 0; i <arguments.length; ++i) {

				var prop;
				src = arguments[i];
				names = Object.getOwnPropertyNames(src);

				for(j = 0; j <names.length; ++j) Object.defineProperty(this, names[j], Object.getOwnPropertyDescriptor(src,names[j]));
				for(j = 0; j <neprops.length; ++j) {

					prop = neprops[j];
					if(src.hasOwnProperty(prop))
						Object.defineProperty(this, prop, Object.getOwnPropertyDescriptor(src,prop));
				}
			}
			var neprops = [

				"valueOf",
				"toString",
				"toLocalString",
				"constructor",
				"hasOwnProperty",
				"isPrototypeOf",
				"propertyIsEnumerable"
			]
		}
	}
)

