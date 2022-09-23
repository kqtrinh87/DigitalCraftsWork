// 3. In JavaScript, create a function that receives an array of numbers and returns an array containing only the positive numbers 

function returnPosNums(inputList) {
    for (let i = 0; i < inputList.length; i++) {
        if (inputList[i] > 0)
            console.log(inputList[i])
    }
}

var inputList = [1, 4 , -5, -11, 5, 0, -9, 13, 24]
returnPosNums(inputList)