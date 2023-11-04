const accordions = document.querySelectorAll('.accordion-header');

for (const accordion of accordions) {
accordion.addEventListener('click', function() {
    accordion.classList.toggle('active');
    const content = accordion.nextElementSibling;
    if (content.style.display === 'block') {
    content.style.display = 'none';
    } else {
    content.style.display = 'block';
    }
});
}