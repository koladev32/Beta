import { userService } from '../api/user.api.js'
import { router } from '../router.js'

const user = JSON.parse(localStorage.getItem('user'));

const initialState = user 
? {status : { loggedIn: true }, user}
: {status : {}, user:null};

export const authentication = {
    namespaced : true,
    state:initialState,
    actions:{
        login({dispatch,commit},{email,password}){
            commit('loginRequest',{email});
            userService.login(email,password)
            .then(
                user => {
                    commit('loginSucess',user);
                    router.push('/');
                },
                error => {
                    commit('loginFailure',error);
                    dispatch('alert/error',error,{root: true});
                }
            );

        },

        logout({commit}){
            userService.logout();
            commit('logout');
        }
    },

    mutations:{
        loginRequest(state,user){
            state.status = { loggedIn : true};
            state.user = user;
        },

        loginSucess(state, user){
            state.status = { loggedIn:true};
            state.user = user;
        },
        loginFailure(state){
            state.status = {};
            state.user = null;
        },
        logout(state){
            state.status = {};
            state.user = null;
        }
    }
}
