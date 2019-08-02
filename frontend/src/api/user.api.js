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
        body:JSON.stringify({email,password})
    };

    return axios.post('http://localhost:8000/api/users/login/', requestOptions)
    .then(handleResponse)
    .then(user => {
        if (user.token){
            localStorage.setItem('user',JSON.stringify(user));
        }
    })
}

function logout(){
    localStorage.removeItem('user');
}

function getAll(){
    const requestOptions = {
        method: 'POST',
        headers : authHeader()
    };

    return axios.get('http://127.0.0.1:8000/api/profiles/laracroft@tomb.com',requestOptions).then(handleResponse);
}

function handleResponse(response){
    return response.text().then( text => {
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
    });
}