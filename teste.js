const axios = require('axios');

async function getToken() {
    const apiEndpoint = 'https://api.mailpro.com/v3/token';

const requestData = new URLSearchParams();

requestData.append('grant_type', 'password');

requestData.append('username', 'mariavjs@al.insper.edu.br'); // Substitua com o seu nome de usuário

requestData.append('password', '914af416-db21-4581-9a3f-dcd92b121676'); // Substitua com a sua senha da API

const options = {

    headers: {
    
    'accept': 'application/json',
    
    'Content-Type': 'application/x-www-form-urlencoded', 
    
    },
    
    }
    
    axios
    
    .post(apiEndpoint, requestData, options)
    
    .then((response) => console.log(response))

}

getToken();


