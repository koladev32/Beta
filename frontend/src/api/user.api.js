import { authHeader } from '../_helpers/auth-header.js'
import axios from "axios"


export const userService = {
    login,
    logout,
    getAll
};

function login(email,password){
    const requestOptions = {
        method : 'POST',
        headers : {'Content-Type':'application/json'},
        user: {
                "email": email,
                "password": password
            }
    };

    return axios.post('http://localhost:8000/api/users/login/', requestOptions)
    .then(handleResponse)
    .then(user=>{
        if (user.token){
            localStorage.setItem('user',JSON.stringify(user));
        }
        return user;
    })
}

function logout(){
    localStorage.removeItem('user');
}

async function getAll(){
    const requestOptions = {
        method: 'GET',
        headers : authHeader()
    };

    const response = await axios.get('http://127.0.0.1:8000/api/profiles/laracroft@tomb.com', requestOptions);
    return handleResponse(response);
}

function handleResponse(response){
    return response.data;/*text().then( text => {
        const data = text && JSON.parse(text);
        if (!response.ok){
            if (response.status === 401){
                logout();
                location.reload(true);
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });*/
}