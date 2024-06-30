document.addEventListener('DOMContentLoaded', function () {
    const items = document.querySelectorAll('.carrusel-item');
    const dotsContainer = document.querySelector('.carrusel-dots');
    let currentIndex = 0;
    const intervalTime = 3000; // Intervalo de tiempo para el cambio de imagen

    // Crear los puntos para la navegación del carrusel
    items.forEach((_, index) => {
        const dot = document.createElement('button');
        dot.classList.add('dot');
        if (index === 0) dot.classList.add('active');
        dot.addEventListener('click', () => {
            clearInterval(autoSlide);
            showSlide(index);
        });
        dotsContainer.appendChild(dot);
    });

    const dots = document.querySelectorAll('.carrusel-dots .dot');

    function showSlide(index) {
        items.forEach((item, i) => {
            item.classList.remove('active');
            item.style.left = i > index ? '100%' : i < index ? '-100%' : '0';
            dots[i].classList.remove('active');
        });
        items[index].classList.add('active');
        dots[index].classList.add('active');
        currentIndex = index;
    }

    // Función para el cambio automático de imágenes
    function nextSlide() {
        const nextIndex = (currentIndex + 1) % items.length;
        showSlide(nextIndex);
    }

    const autoSlide = setInterval(nextSlide, intervalTime);
});
