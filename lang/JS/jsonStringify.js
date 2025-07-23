

var jsonStringify = function(O) {

    if(Array.isArray(O)) return "[" + O.map(E => jsonStringify(E)).join() + "]";
    if(O && typeof O === "object")
        return "{" + Array.prototype.map.call(Object.keys(O),K => `${jsonStringify(K)}:${jsonStringify(O[K])}`).join() + "}"
    if(typeof(O) === "string") return `"${O}"`;
    return String(O)
}

