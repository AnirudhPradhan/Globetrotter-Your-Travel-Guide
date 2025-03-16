document.addEventListener("DOMContentLoaded", function() {
    var navbarToggle = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.querySelector('.navbar-collapse');

    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    navbarToggle.addEventListener('click', function(event) {
        event.preventDefault();
        navbarCollapse.classList.toggle('show');
        scrollToTop();
    });

    var navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(function(navLink) {
        navLink.addEventListener('click', function() {
            navbarCollapse.classList.remove('show');
        });
    });

    document.body.addEventListener('click', function(event) {
        if (!event.target.closest('.navbar')) {
            scrollToTop();
        }
    });
});
