import { userService } from '../api/user.api'

export const users = {
    namespaced:true,
    state:{
        all:{}
    },

    actions:{
        getAll({ commit }){
            commit('getAllRequest');

            userService.getAll().then(
                users => commit('getAllsucess',users),
                error => commit('getAllFailure',error)
            );
        }
    },
    mutations: {
        getAllRequest(state){
            state.all = { loading:true };

        },
        getAllsucess(state,users){
            state.all = { items:users};
        },
        getAllFailure(state,error){
            state.all = { error }
        }
    }
}