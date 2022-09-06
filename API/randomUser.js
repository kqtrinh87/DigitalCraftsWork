let userButton = document.getElementById('userButton');
let avatarImage = document.getElementById('avatar-img');
let userTitle = document.getElementById('userTitle');
let message = document.getElementById('overview');
let bioinfo = document.getElementById('bioinfo')
let index = 0;
let users = [];
const body = document.getElementsByTagName('body');


const getUser = () => {
    fetch('https://random-data-api.com/api/v2/users?size=100')
    .then(response => {
        return response.json();
    })
    .then(userData => {
        userData.forEach(user => {
            
        })      
        console.log(userData);
        
        displayCard(userData, index);

        users = userData;
        
    
    })
}
window.onload=getUser();

const displayCard = (userData, index) => {
    
    // Step 1: Get the user image
    let avatar = userData[index].avatar;
    console.log(avatar);

    // Step 2: Place the image inside of our card
    avatarImage.src = avatar;

    // Step 3: Set Card Title to username
    let username = userData[index].username;
    userTitle.innerText = username; 

    // Step 4: Set card data to a introductory message
    message.innerText = 'Hi my name is ' + userData[index].first_name + ' ' + userData[index].last_name + ' I am a ' + userData[index].employment.title;
    // Add a more info button that displays First Name, last name, state, country, and subscription status in a tooltip
    bioinfo.innerText = `First name: ${userData[index].first_name}\n Last name: ${userData[index].last_name}\n State: ${userData[index].address.state}\n Country: ${userData[index].address.country}\n Subscription Status: ${userData[index].subscription.status}`
}

const previousCard = () => {
    if(index>0) {
        index--;
        displayCard(users, index);
    }
}

const nextCard = () => {
    if (index < 99) {
        index++;
        displayCard(users, index)
}
}

// const newPreviousButton = document.createElement('button');
        // newPreviousButton.innerText = "Previous";
        // newPreviousButton.onload = "previousCard()";

        // const newNextButton = document.createElement('button');
        // newPreviousButton.innerText = "Next";
        // newPreviousButton.onload = "nextCard()";

        // body.append(newPreviousButton);
        // body.append(newNextButton);

