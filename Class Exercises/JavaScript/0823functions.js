// This is a basic function
function area(length, width) {
    return length * width;
}

// Arrow function
let circumference = (radius) => {
    const PI = 3.14;
    return PI * (radius^2)
}

console.log(circumference(5))

// Anonyomous Function
const sum = function(number1, number2) {
    return number1 + number2;
}

console.log(sum(3, 7))



