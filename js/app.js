// Untuk Navbar
function toggleMenu() {
    var navbar = document.getElementById("navbar");
    var navbarOpenIcon = document.getElementById("navbar-open");
    var navbarCloseIcon = document.getElementById("navbar-close");
    if (navbar.classList.contains("hidden")) {
        navbar.classList.remove("hidden");
        navbarCloseIcon.classList.remove("hidden");
        navbarOpenIcon.classList.add("hidden");
    } else {
        navbar.classList.add("hidden");
        navbarCloseIcon.classList.add("hidden");
        navbarOpenIcon.classList.remove("hidden");
    }
}

// Untuk Hidden Password atau View Password
document.querySelectorAll('.js-password-toggle').forEach(passwordToggle => {
    passwordToggle.addEventListener('change', function () {
        const parent = this.closest('.relative');
        const password = parent.querySelector('.js-password');
        const passwordLabel = parent.querySelector('.js-password-label');

        if (password.type === 'password') {
            password.type = 'text';
            passwordLabel.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
        } else {
            password.type = 'password';
            passwordLabel.innerHTML = '<i class="fa-solid fa-eye"></i>';
        }

        password.focus();
    });
});
