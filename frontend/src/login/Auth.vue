<template>
    <div class="limiter">
        <div class="container-login100">
            <div class="wrap-login100">
                <div class="login100-pic js-tilt" data-tilt>
                    <img src="images/img-01.png" alt="IMG">
                </div>
                <form class="login100-form validate-form" @submit.prevent="handleSubmit" method="post">
                    <span class="login100-form-title">
                        Member Login
                    </span>
                    <div class="wrap-input100 validate-input" data-validate="Valid email is required: ex@abc.xyz">
                        <input class="input100" type="text" name="email" placeholder="Email" v-validate="'required'" v-model="user.email" :class="{'is-invalid' : submitted && !email}">
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="fa fa-envelope" aria-hidden="true"></i>
                        </span>
                    </div>
                    <div class="wrap-input100 validate-input" data-validate="Password is required">
                        <input class="input100" type="password" name="password" placeholder="Password" v-validate="'required'" v-model="user.password" :class="{'is-invalid':submitted && !password}">
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="fa fa-lock" aria-hidden="true"></i>
                        </span>
                    </div>
                    <div class="container-login100-form-btn">
                        <button class="login100-form-btn" type="submit" :disabled="logginIn">
                            Login
                        </button>
                    </div>
                    <div class="text-center p-t-12">
                        <span class="txt1">
                            Forgot
                        </span>
                        <a class="txt2" href="#">
                            Username / Password?
                        </a>
                    </div>
                    <div class="text-center p-t-136">
                        <a class="txt2" href="#">
                            Create your Account
                            <i class="fa fa-long-arrow-right m-l-5" aria-hidden="true"></i>
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            email:'',
            password:'',
            submitted:false
        }
    },
    computed:{
        loggingIn(){
            return this.$store.state.authentication.status.loggingIn;
        }
    },
    created(){
        //reset login status
        this.$store.dispatch('authentication/logout');
    },

    methods:{
        handleSubmit(e){
            this.submitted = true;
            const {email,password} = this;
            const {dispatch} = this.$store;
            if(email && password){
                dispatch('authentication/login',{email,password});
            }
        }
    }
}

</script>

<style src="../css/main.css"></style>