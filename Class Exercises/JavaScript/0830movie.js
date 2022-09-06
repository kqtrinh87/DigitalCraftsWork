const list = document.getElementById('movieList');

const getMovie = () => {
    nameList = [];
    picList = [];
    fetch('https://api.themoviedb.org/3/movie/popular?api_key=///')
    .then(response => {
        return response.json();
    })
    .then(data => {
        // console.log(data)
        
        for(let i = 0;i<5;i++) {
            // displayMovieTitle.innerText = data.results[i].title
            nameList.push(data.results[i].title);
            console.log(nameList);
            const newMovie = document.createElement('h4');
            newMovie.innerText = nameList[i];
            list.append(newMovie);

            picList.push("https://image.tmdb.org/t/p/w220_and_h330_face/" + data.results[i].poster_path)
            console.log(picList);
            const newPoster = document.createElement('img')
            newPoster.src = picList[i];
            list.append(newPoster);
            

            // form.reset();
        }
    })
}

// const displayMovieTitle = document.getElementById('getMovie')
// const displayMoviePoster = document.getElementById('getPoster')
// const displayMovie1 = document.getElementById('movie1')

// const getMovie = () => {
//     nameList = [];
//     picList = [];
//     fetch('https://api.themoviedb.org/3/movie/popular?api_key=feff74a65c3f6c60cee2fb245f22ebfb')
//     .then(response => {
//         return response.json();
//     })
//     .then(data => {
//         console.log(data)
        
//         for(let i = 0;i<5;i++) {
//         displayMovieTitle.innerText = data.results[i].title
//             nameList.push(data.results[i].title);
//             console.log(nameList);
//         }
//     })
// }
// getMovie();

// displayMovie1.innerText = movie1
// let movie1 = nameList[0]
// let movie2 = nameList[1]
// let movie3 = nameList[2]
// let movie4 = nameList[3]
// let movie5 = nameList[4]
