document.addEventListener('DOMContentLoaded', () => {
    const likeButton = document.getElementById('like-button');
    const dislikeButton = document.getElementById('dislike-button');
    const likeCount = document.getElementById('like-count');
    const dislikeCount = document.getElementById('dislike-count');
    const commentForm = document.getElementById('comment-form');
    const newComment = document.getElementById('new-comment');
    const commentsSection = document.getElementById('comments');

    let likeActive = false;
    let dislikeActive = false;

    if (!likeButton || !dislikeButton || !likeCount || !dislikeCount) {
        console.error('Error: No se pudieron encontrar uno o más elementos.');
        return;
    }

    likeButton.addEventListener('click', () => {
        if (!likeActive) {
            likeCount.textContent = parseInt(likeCount.textContent) + 1;
            likeButton.classList.add('active');
            if (dislikeActive) {
                dislikeCount.textContent = parseInt(dislikeCount.textContent) - 1;
                
dislikeButton.classList.remove('active');
                dislikeActive = false;
            }
            likeActive = true;
        } else {
            likeCount.textContent = parseInt(likeCount.textContent) - 1;
            likeButton.classList.remove('active');
            likeActive = false;
        }
    });

    dislikeButton.addEventListener('click', () => {
        if (!dislikeActive) {
            dislikeCount.textContent = parseInt(dislikeCount.textContent) + 1;
            dislikeButton.classList.add('active');
            if (likeActive) {
                likeCount.textContent = parseInt(likeCount.textContent) - 1;
                likeButton.classList.remove('active');
                likeActive = false;
            }
            dislikeActive = true;
        } else {
            dislikeCount.textContent = parseInt(dislikeCount.textContent) - 1;
            dislikeButton.classList.remove('active');
            dislikeActive = false;
        }
    });

    commentForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const commentText = newComment.value.trim();
        if (commentText) {
            const comment = document.createElement('div');
            comment.className = 'comment';

            const author = document.createElement('div');
            author.className = 'comment-author';
            author.textContent = 'Usuario Anónimo'; // Aquí puedes añadir funcionalidad para el nombre del usuario

            const text = document.createElement('div');
            text.className = 'comment-text';
            text.textContent = commentText;

            comment.appendChild(author);
            comment.appendChild(text);
            commentsSection.appendChild(comment);

            newComment.value = '';
        }
    });
});