/* Write a function leetspeak which is given a string, and returns the 
leetspeak equivalent of the string. To convert text to its leetspeak version, 
make the following substitutions: 
A => 4 E => 3 G => 6 I => 1 O => 0 S => 5 T => 7 */

// Given a string

let userInput = "Testing";
let convertedLeetSpeak = '';

// Scan through each letter of the string
let leetspeak = (userInput) => {
    for(let i = 0; i < userInput.length; i++);
        convertedLeetSpeak.push(userInput)
    /* let a variable equal to zero, continue
     until the variable is less than the length of the array, increment by 1*/
        console.log(convertedLeetSpeak);
    /* print out the array of each index whatever the variable is */
    }
// If it's not A, E, G, I, O, S, or T, append it to a list
// If it's A, add a 4 to the list
// If it's E, add a 3 to the list
// If it's G, add a 6 to the list
// If it's I, add a 1 to the list
// If it's O, add a 0 to the list
// If it's S, add a 5 to the list
// If it's T, add a 7 to the list
//Print out final list
console.log(convertedLeetSpeak)

