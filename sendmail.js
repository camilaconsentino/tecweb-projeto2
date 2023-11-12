import axios from "axios";
import React, { useState } from "react";

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
      
  
      const response = await axios.post(apiEndpoint, requestData, options);
  
      const token = response.data.access_token;
    
      return token;
  
      
  }
  //getToken();
  
  // Fazendo a requisição do email
  
  async function sendMail(user, name) {
      try {
          const bearerToken = await getToken();
          
          const email = {
              email: user,
              id_sender_email: 322291,
              body_html: `Olá ${name}, bem vinde a nossa familia! Entre no site para marcar sua primeira aula`,
              date_planned: null,
              subject: 'Bem Vinde!!',
          };
  
              const headers = {
  
                  'Authorization': `Bearer ${bearerToken}`,
                  
                  'Content-Type': 'application/json',

                  'Access-Control-Allow-Origin': '*',
                  
                  };
                  
                  
              const config = {
                  
                  method: 'POST',
                  
                  url: "https://api.mailpro.com/v3/send/mail",
                  
                  headers: headers,
                  
                  data: JSON.stringify(email)
                  
                  };
                
            
            
              
              axios(config).then((response) => console.log(response.data));

  
            
              const response = await axios.post("http://localhost:8000/api/send-email-proxy", data);
            } catch (error) {
          console.error(error);
      }
  }

sendMail();