const express = require('express')
const logger = require('./logger')
const ejs = require('ejs')
let todo = require('./database')

const app = express()
app.use(express.json())

app.set("view engine", "ejs")

app.all('*', (req, res, next) => {
    logger.info({
        "time" : new Date(),
        "path" : req.path,
        "body" : req.body,
        "method" : req.method
    })
    next()
})

app.get('/', function (req, res){
    if (Object.keys(req.body).length == 0){
        res.send(todo)
    }
    else{
        logger.error({
            "time" : new Date(),
            "message" : `User tried to pass a body, '${req.body}', into GET method.`,
            "path" : req.path,
            "method" : req.method
        })
        res.statusCode = 400
        res.send('You cannot pass a body to a GET call.')
    }
})

app.get('/todos', function (req, res){
    if (Object.keys(req.body).length == 0){
        res.render("todolist", { todo: todo} )}
    else {
        logger.error({
            "time" : new Date(),
            "message" : `User tried to pass a body, '${req.body}', into GET method.`,
            "path" : req.path,
            "method" : req.method
        })
        res.statusCode = 400
        res.send('You cannot pass a body to a GET call.')
    }
})

app.get('/todo', function (req, res){
    if (Object.keys(req.body).length == 0){
        let found = false
        for (let i = 0; i < todo.length; i++){
            if (todo[i].task == req.query.task){
                found = true
                res.send(todo[i])
            }
        }
        if (found == false){
            logger.error({
                "time" : new Date(),
                "message" : `User tried to search for ${req.query.task}`,
                "path" : req.path,
                "method" : req.method
            })
            res.statusCode = 400
            res.send('The task does not exist.')
        }
    }
    else{
        logger.error({
            "time" : new Date(),
            "message" : `User tried to pass a body, '${req.body}', into GET method.`,
            "path" : req.path,
            "method" : req.method
        })
        res.statusCode = 400
        res.send('You cannot pass a body to a GET call.')
    }
})

app.post('/todo', function (req, res) {
    let posted = false
    let found = false
    for (let i = 0; i < todo.length; i++){
        if (req.body.task.toLowerCase() == todo[i].task.toLowerCase()){
            found = true
            logger.error({
                "time" : new Date(),
                "message" : `User tried to post '${req.body.task}', which already exists`,
                "path" : req.path,
                "method" : req.method
            })
            res.send(`This task already exists.`)
        }}
    if (typeof(req.body.task) == 'string' && req.body.task != '' && found == false){
        newTodo = {"task": req.body.task}
        todo.push(newTodo)
        posted = true
        res.send(`The task '${req.body.task}' has been added to the to-do list.`)
    }
    if (posted == false && found == false){
        logger.error({
            "time" : new Date(),
            "message" : `User tried to post '${req.body.task}', which was invalid`,
            "path" : req.path,
            "method" : req.method
        })
        res.statusCode = 400
        res.send(`This was an invalid entry.`)
    }
})

app.delete('/todo/:task', function (req, res) {
    if(Object.keys(req.body).length == 0){
        let deleted = false
        for (let i = 0; i < todo.length; i++){
            if (todo[i].task == req.params.task){
                tempTask = todo[i].task
                todo.splice(i, 1)
                deleted = true
                res.send(`'${tempTask}' was removed from to-do list.`)
            }
        }
        if (deleted == false){
            logger.error({
                "time" : new Date(),
                "message" : `User tried to delete '${req.params.task}', which does not exist.`,
                "path" : req.path,
                "method" : req.method
            })
            res.statusCode = 400
            res.send('Task does not exist.')
        }
    }
    else{
        logger.error({
            "time" : new Date(),
            "message" : `User tried to pass a body, '${req.body}', into DELETE method.`,
            "path" : req.path,
            "method" : req.method
        })
        res.statusCode = 400
        res.send('You cannot pass a body to a DELETE call.')
    }
})

app.put('/todo/:task', function (req, res) {
    let found = false
    for (let i = 0; i < todo.length; i++){
        if (todo[i].task == req.params.task){
            if (typeof(req.body.task) == 'string' && req.body.task != ''){
                modifiedTask = {"task" : req.body.task}
                todo[i] = modifiedTask
                found = true
                res.send(`Task '${req.params.task}' was modified to '${req.body.task}'`)
            }
        }
    }
    if (found == false) {
        logger.error({
            "time" : new Date(),
            "message" : `User tried to change '${req.params.task}', which may not exist, to '${req.body.task}', which may be invalid.`,
            "path" : req.path,
            "method" : req.method
        })
        res.statusCode = 400
        res.send('Task does not exist or the body did not contain a task.')
    }   
})

app.listen(3000)
console.log("Server is running on port 3000") 