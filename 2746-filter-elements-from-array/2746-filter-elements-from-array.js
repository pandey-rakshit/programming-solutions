/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    result = []

    for(let i = 0; i < arr.length; i++){
        outputFn = fn(arr[i], i)
        if (!!outputFn){
            result.push(arr[i])
        }
    }

    return result
};