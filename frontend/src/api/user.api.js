import { authHeader } from '../_helpers/auth-header.js'
import axios from "axios"


export const userService = {
    login,
    logout,
    getAll
};

async function login(email,password){
    const requestOptions = {
        method : 'POST',
        headers : {'Content-Type':'application/json'},
        body: JSON.stringify({email,password})
    };

    const response = await axios.post('http://localhost:8000/api/users/login/', requestOptions);
    const user = await handleResponse(response);
    if (user.token) {
        localStorage.setItem('user', JSON.stringify(user));
    }
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