document.addEventListener("DOMContentLoaded", function() {
    var navbarToggle = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.querySelector('.navbar-collapse');

    navbarToggle.addEventListener('click', function(event) {
        event.preventDefault();
        
        navbarCollapse.classList.toggle('show');
        
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    var navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(function(navLink) {
        navLink.addEventListener('click', function() {
            navbarCollapse.classList.remove('show');
        });
    });
});
