// submit = document.getElementsByTagName('button');
// submit[0].addEventListener('click', submitInfo);
// const nameList = document.createElement('li');
nameList = [];

form = document.getElementById('teamform')

// function submitInfo(event) {
form.addEventListener('submit',function(event) {
    event.preventDefault();
    firstname = document.getElementById('firstname').value;
    lastname = document.getElementById('lastname').value;
    phone = document.getElementById('phonenumber').value;
    email = document.getElementById('email').value;
    password = document.getElementById('password').value;

    let info = {
        'firstname': firstname,
        'lastname': lastname,
        'phone': phone,
        'email': email,
        'password': password
    }

    nameList.push(info);
    form.reset();
    console.log(nameList);
})

