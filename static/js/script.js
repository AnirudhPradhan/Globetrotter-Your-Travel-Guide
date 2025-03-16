document.addEventListener("DOMContentLoaded", function() {
    var navbarToggle = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.querySelector('.navbar-collapse');

    // Function to scroll to top
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    // Navbar toggle functionality
    navbarToggle.addEventListener('click', function(event) {
        event.preventDefault();
        navbarCollapse.classList.toggle('show');
        scrollToTop();
    });

    // Close the navbar when a link is clicked
    var navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(function(navLink) {
        navLink.addEventListener('click', function() {
            navbarCollapse.classList.remove('show');
        });
    });

    // Scroll to top when clicking anywhere on the page
    document.body.addEventListener('click', function(event) {
        // Check if the click is not on or within the navbar
        if (!event.target.closest('.navbar')) {
            scrollToTop();
        }
    });
});
