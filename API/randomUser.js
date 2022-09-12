let userButton = document.getElementById('userButton');
let cardArray = document.getElementById('cardArray');
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
        // console.log(userData);
        
        displayCard(userData);

        users = userData;
        
    
    })
}
window.onload=getUser(); //Load the profiles as soon the page loads

const displayCard = (userData) => {
    index = 0;
    userData.forEach(() => {
        
        // newCard = document.createElement('div');
        // newCard.innerHTML = `
        // <div class="card" style="width: 18rem;">
        //     <!-- XBOX Users Avatar -->
        //     <img id="avatar-img${index}" src="." class="card-img-top" alt="...">
        //     <div id="card-body${index}" class="card-body">
        //         <!-- Username -->
        //     <h5 id="userTitle${index}" class="card-title">.</h5>
        //     <p id="overview${index}" class="card-text">.</p>
        //         <div class="extraBox">
        //             <button class="btn btn-secondary">Learn More</button>
        //             <p class="extraBoxText" id="bioinfo${index}">Tooltip text</p>
        //         </div>
        //     </div>`

        // let avatarImage = document.getElementById(`avatar-img${index}`);
        // let userTitle = document.getElementById(`userTitle${index}`);
        // let message = document.getElementById(`overview${index}`);
        // let bioinfo = document.getElementById(`bioinfo${index}`);
        
        // Step 1: Get the user image
        let avatar = userData[index].avatar;
        console.log(avatar);

        // Step 2: Place the image inside of our card
        // avatarImage.src = avatar;

        // Step 3: Set Card Title to username
        let username = userData[index].username;
        //userTitle.innerText = username; 

        // Step 4: Set card data to a introductory message
        let userMessage = 'Hi my name is ' + userData[index].first_name + ' ' + userData[index].last_name + ' I am a ' + userData[index].employment.title;
        // message.innerText = 
        // Add a more info button that displays First Name, last name, state, country, and subscription status in a tooltip
        let bioinfo = `First name: ${userData[index].first_name}\n Last name: ${userData[index].last_name}\n State: ${userData[index].address.state}\n Country: ${userData[index].address.country}\n Subscription Status: ${userData[index].subscription.status}`
        // bioinfo.innerText = `First name: ${userData[index].first_name}\n Last name: ${userData[index].last_name}\n State: ${userData[index].address.state}\n Country: ${userData[index].address.country}\n Subscription Status: ${userData[index].subscription.status}`
        
        newCard = document.createElement('div');
        newCard.innerHTML = `
        <div class="card" style="width: 18rem;">
            <!-- XBOX Users Avatar -->
            <img id="avatar-img" src="${avatar}" class="card-img-top" alt="...">
            <div id="card-body" class="card-body">
                <!-- Username -->
            <h5 id="userTitle" class="card-title">${username}</h5>
            <p id="overview" class="card-text">${userMessage}</p>
                <div class="extraBox">
                    <button class="btn btn-secondary">Learn More</button>
                    <p class="extraBoxText" id="bioinfo">${bioinfo}</p>
                </div>
            </div>`
        cardArray.append(newCard);
        index++
        })
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
