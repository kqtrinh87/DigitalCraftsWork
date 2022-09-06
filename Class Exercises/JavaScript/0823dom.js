function getUserInfo() {
    username = document.getElementById('username-box').value;
    // This will take the username input as a string
    password = document.getElementById('password-box').value;
    console.log(`Username: ${username}, Password: ${password}`);
}

function checkUsername(username) {
    // Check username valid character input
    let myRegex = /[A-Za-z]+/
    return myRegex.test(username)
}


function checkPassword(username, password) {
    let mockDb = new Map();
    mockDb.set('kqtrinh', 'password');

    // Check only
let myRegex = /[A-Za-z0-9]+/
}
    // Checking to see the username is in the database
    // Username was not found
    if(mockDb.get(username) == undefined) {
        alert('No account found with that username.')
    // Check if password matches wha tis in the database
    } else if ((mockDb.get(username)) == password) {// ??? 
        alert('You are signed in.');
    } else {
        alert('Incorrect password.');
    }
