/* eslint-disable no-undef */
import axios from "axios"

function login(email,pass){
    var data = JSON.stringify(
        {
            "user":{
                    "email":email,
                    "pass":pass
            }
        }
    );

    axios.post('http://127.0.0.1:8000/api/users/login/',data,{
        headers:{

        }
    })
    .then(res => {
        // eslint-disable-next-line no-console
        var token = JSON.parse(res).token;
    })
    .catch(err => {
        Console.error(err); 
    })
}