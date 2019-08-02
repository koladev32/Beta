<template>
    <div>
        Welcome {{user.LastName}}
        <router-link to="/login" >Logout</router-link>
    </div>
</template>

<script>
export default {
    computed:{
        user () {
            return this.$store.state.authentication.user;
        },
        
    },
    created(){
        this.$store.dispatch('users/getAll');
    }
};
</script>