// axios vr represents the code that we just installed
const axios = require('axios');

axios.get('http://api.open-notify.org/astros.json')

    .then(response => {
        console.log(response.data);

    })

    .catch(error => {
        console.log(error);
    
    });

