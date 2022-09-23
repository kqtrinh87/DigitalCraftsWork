let axios = require('axios').default;
let http = require('http');
const { hostname } = require('os');
// const axios = require('axios')

const host ='127.0.0.1'; // The numerical address for localhost
const port = 8080;

const anotherPort = 8001

// Creating a server that can accept API calls
const server = http.createServer((req, res) => {
    res.statusCode = 200
    res.setHeader('Content-Type', 'text/plain');
    res.end(`You're reached my server`)
})

server.listen(port, host, () => {
    console.log(`The server is running at http:${host}:${port}`)
})

// Creating another server running on a different port. Ports can only run one application at a time.

const anotherServer = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end(`You're reached my OTHER server`)
})

server.listen(port, host, () => {
    console.log(`The server is running at http:${host}:${anotherPort}`)
})
