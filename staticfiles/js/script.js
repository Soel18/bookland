document.addEventListener('DOMContentLoaded', function () {
    const body = document.querySelector("body"),
          nav = document.querySelector("nav"),
          modeToggle = document.querySelector(".dark-light"),
          searchToggle = document.querySelector(".searchToggle"),
          sidebarOpen = document.querySelector(".sidebarOpen"),
          genreList = document.getElementById('genre-list'),
          books = document.querySelectorAll('.book');

    let getMode = localStorage.getItem("mode");
    if (getMode && getMode === "dark-mode") {
        body.classList.add("dark");
    }

    // Alternar modo oscuro y claro
    modeToggle.addEventListener("click", () => {
        modeToggle.classList.toggle("active");
        body.classList.toggle("dark");

        if (!body.classList.contains("dark")) {
            localStorage.setItem("mode", "light-mode");
        } else {
            localStorage.setItem("mode", "dark-mode");
        }
    });

    // Alternar caja de búsqueda
    searchToggle.addEventListener("click", () => {
        searchToggle.classList.toggle("active");
    });

    // Alternar barra lateral
    sidebarOpen.addEventListener("click", () => {
        nav.classList.add("active");
    });

    // Cerrar la barra lateral al hacer clic fuera de ella
    body.addEventListener("click", (e) => {
        let clickedElm = e.target;

        if (!clickedElm.classList.contains("sidebarOpen") && !clickedElm.classList.contains("menu")) {
            nav.classList.remove("active");
        }
    });

    // Filtrar libros por género

    function filterBooks(genre) {
        books.forEach(book => {
            if (genre === 'todos' || book.getAttribute('data-genre') === genre) {
                book.style.display = 'block';
            } else {
                book.style.display = 'none';
            }
        });
    }

    // Carrusel de géneros
    const carousels = document.querySelectorAll('.carousel');

    carousels.forEach(carousel => {
        const bookList = carousel.querySelector('.book-list');
        const nextButton = carousel.querySelector('.carousel-button.next');
        const prevButton = carousel.querySelector('.carousel-button.prev');

        const scrollPerClick = 300; // Ajusta este valor según sea necesario

        nextButton.addEventListener('click', () => {
            bookList.scrollBy({ left: scrollPerClick, behavior: 'smooth' });
        });

        prevButton.addEventListener('click', () => {
            bookList.scrollBy({ left: -scrollPerClick, behavior: 'smooth' });
        });
    });
});

/* Js de genero de libros */
 document.addEventListener('DOMContentLoaded', function() {
                const carousels = document.querySelectorAll('.carousel');
    
                carousels.forEach(carousel => {
                    const prevButton = carousel.querySelector('.prev');
                    const nextButton = carousel.querySelector('.next');
                    const bookList = carousel.querySelector('.book-list');
    
                    prevButton.addEventListener('click', function() {
                        bookList.scrollBy({
                            left: -bookList.clientWidth,
                            behavior: 'smooth'
                        });
                    });
    
                    nextButton.addEventListener('click', function() {
                        bookList.scrollBy({
                            left: bookList.clientWidth,
                            behavior: 'smooth'
                        });
                    });
                });
            });

/* Js de escritores */
document.querySelectorAll('.follow-btn').forEach(button => {
    button.addEventListener('click', () => {
        alert('Has seguido a este escritor');
    });
});

document.querySelectorAll('.favorite-btn').forEach(button => {
    button.addEventListener('click', () => {
        alert('Has marcado a este escritor como favorito');
    });
});
