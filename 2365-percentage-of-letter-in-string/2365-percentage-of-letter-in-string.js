/**
 * @param {string} s
 * @param {character} letter
 * @return {number}
 */
var percentageLetter = function(s, letter) {
    count = 0
    for (const e of s){
        if (e === letter){
            count += 1
        }
    }

    const percentage = Math.floor((count / s.length)*100)
    return percentage
    
};