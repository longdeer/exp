var checkIfInstanceOf = function(obj, classFunction) {

    if(classFunction === undefined) return false;
    if(classFunction === null) return false;
    if(obj === undefined) return false;
    if(obj === null) return false;

    return  classFunction.prototype === Object.getPrototypeOf(obj) ? true :
            checkIfInstanceOf(Object.getPrototypeOf(obj), classFunction);
}