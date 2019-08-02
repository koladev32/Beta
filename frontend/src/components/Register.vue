<template>
    <div class="limiter">
        <div class="container-login100">
            <div class="wrap-login100">
                <div class="login100-pic js-tilt" data-tilt>
                    <img src="images/img-01.png" alt="IMG">
                </div>
                <form class="login100-form validate-form">
                    <span class="login100-form-title">
                        Register here.
                    </span>

                    <div class="wrap-input100 validate-input" data-validate="Last name is required.">
                        <input class="input100" type="text" name="lastname" placeholder="Last Name">
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="fa fa-envelope" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="wrap-input100 validate-input" data-validate="First name is required.">
                        <input class="input100" type="text" name="firstname" placeholder="First Name">
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="fa fa-envelope" aria-hidden="true"></i>
                        </span>
                    </div>

                    <div class="wrap-input100 validate-input" data-validate="Valid email is required: ex@abc.xyz">
                        <input class="input100" name="email" placeholder="Email">
                        <span class="focus-input100"></span>
                        <span class="symbol-input100">
                            <i class="fa fa-envelope" aria-hidden="true"></i>
                        </span>
                    </div>
                    <span class="columns">
                        <span class="wrap-input100 validate-input column" data-validate="Birth Date is required.">
                            <input class="input100" type="date" name="birthdate" placeholder="Birth date">
                            <span class="focus-input100"></span>
                            <span class="symbol-input100">
                                <i class="fa fa-envelope" aria-hidden="true"></i>
                            </span>
                        </span>

                        <span class="wrap-input100 validate-input column" data-validate="Birth Date is required.">
                            <input class="input100" type="option" name="birthdate" placeholder="Birth date">
                            <span class="focus-input100"></span>
                            <span class="symbol-input100">
                                <i class="fa fa-envelope" aria-hidden="true"></i>
                            </span>
                        </span>
                    </span>

                    <div class="container-login100-form-btn">
                        <button class="login100-form-btn">
                            Submit
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    export default {

    }
</script>

<style src="../css/main.css">
</style>