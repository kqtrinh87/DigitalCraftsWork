const displayTemp = document.getElementById('temperature');
const heatIndex = document.getElementById('realfeel')


const getWeather = () => {
    let currentWeather = {
        temp: 0,
        // realFeel: 0,
        // cloudyCover: ''
    }
    // Query parameters by a ?
    fetch('https://api.openweathermap.org/data/2.5/weather?lat=29.749907&lon=-95.358421&appid=///')
    // Response is stored in a response variable (doesn't have to called response, can be called whatever)
    .then(response => { 
        let object = response;
        // response.json()
        return response.json();
    }

)
    .then(data =>
        displayTemp.innerText = math.round(data.main.temp)
        heatIndex.innerText = math.round(data.main.feels_like)
        // currentWeather.realFeel = data.main.feel_like
        // console.log(data.main.temp)
        ); 

// Code running down here
}

// Promises: a contract in your code, that promises that a variable will be 
// assigned at some point in the future

// Promise: Pending, Fulfilled, Cancelled or Rejected
