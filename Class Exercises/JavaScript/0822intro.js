// This is a JavaScript comment
/* This is a block
   comment in JavaScript */

/* JS Types:
    number,
    string,
    boolean,
    object,
    array,
*/

// This is how you declare a variable
var myname = 'Khanh Trinh';
console.log(myname);

// This is how you declare a variable with modern JS
let city = 'Houston';
console.log(city);

// In JS, we must declare our constants
const PI = 3.14;
// PI = 5;    It will crash because you cannot change constant variable
console.log(PI)

// JS uses the number class instead of integer
console.log(typeof(35)); // Type: Number
console.log(typeof(35.45)); // Type: Number (No floats in JS)

// In JS, No captalizing on booleans
isRaining = true;

// Worknig with arrays in JS
let scores = [3, 4, 7, 3];
console.log(scores);

// To find the length of an array, use the length that belongs to the array class
console.log(scores.length);

// Object
let player = {
    name: "Ronald Acuna Jr",
    number: 13,
    position: "Right Field",
    IR: false
};

console.log(player);

// Accessing properties within an object
console.log(player.name)

// JS has a built in Date Type
// we use the keyword 'new' to declare a new instant of a class
let todaysDate = new Date();
console.log(todaysDate);

// JS functions have a different keyword to define, JS has 4 ways
function salutations(username) {
    console.log('Hello',username) // #1
    return 'Hello' + username // #2 
};

salutations('Khanh');

// String concatenation

let month = 'August';
let date = 22;
let year = 2022;

// String interpolation, similiar to %d or %s
console.log(`Today is ${month} ${date}, ${year} `)

// JS has incrementors/decrementors, such as 'i += 1'
let count = 0;
count++; // Increment by 1
count++; // Increment by 1
count--; // Decrement by 1
count=+2; // Increment byu 2
console.log(`Count: ${count}`)

// Keywords such as 'and', 'or', etc does not exists
// Check if it is raining and the month is August
// && = 'and'
if (isRaining && month == 'August') {
    console.log(`We're in the dog days of summer.`)
}

// Check if its sunny or the year is 2022
// ! is 'not'   || is 'or'
if(!isRaining || year == 2022) {
    console.log(`No time like the present.`)
}

// Loose Comparsion == vs Strict Comparsion ===
// Loose Comparsion evaluate just the value while strict comparsion
// evaluates the value and the type
if(!isRaining || year === 2022) {
    console.log(`No time like the present.`)
}

console.log(5/2) // 2.5
console.log(5%2) // Remainder of 1

// Conditional statements - if, elif, else
if (!isRaining) {
    console.log('You can go outside.')
} 
else if (isRaining) { //Have to stay arguement
    console.log(`It's raining, stay inside.`)
}

// Switch statements: generally used when we have to check several conditions
let day = new Date().getDay();
console.log(day)
switch (day) {
    case 0: // case is like "if"
        console.log(`It's Sunday.`)
        break;
    case 1:
        console.log(`It's Monday.`)
        break;
    case 2:
        console.log(`It's Tuesday.`)
        break;
    case 3:
        console.log(`It's Wednesday.`)
        break;
    case 4:
        console.log(`It's Thursday.`)
        break;
    case 5:
        console.log(`It's Friday.`)
        break;
    case 6:
        console.log(`It's Saturday.`)
        break;
    default: // It is like "else" from Python
        console.log('Not sure which day of the week it is.')
}

// For loops
let days = ['Sunday', 'Monday','Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']

for(let i = 0; i <days.length; i++) {
/* let a variable equal to zero, continue
 until the variable is less than the length of the array, increment by 1*/
    console.log(days[i]);
/* print out the array of each index whatever the variable is */
}

// While loops
let i = 0; 
while(i<days.length) {
    console.log(days[i]);
    i++;
}

// Iterate backwards in an array
for(let j= days.length -1; j>= 0; j--) {
    console.log(days[j])
}

// Print every day of the week that falls on an odd index
for(let k=1; k < days.length; k+=2) {
    console.log(days[k])
}

