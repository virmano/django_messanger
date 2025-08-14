function createReply(button){
    const replyId = button.dataset.id
    document.querySelector('input[name="reply"]').value = replyId

    container = document.querySelector(".reply-message")
    container.style.display = 'flex'
}

function cancelReply() {
    document.querySelector('input[name="reply"]').value = null
    container = document.querySelector(".reply-message")
    container.style.display = 'none'
}

function showReplies(button) {
    const commentId = button.dataset.id;
    const container = document.getElementById(`replies-${commentId}`);

    if (container.style.display === 'none' || !container.style.display) {
        fetch(`/get_replies/${commentId}/`)
            .then(response => response.text())
            .then(html => {
                container.innerHTML = html;
                container.style.display = 'block';

                container.querySelectorAll('.reply-comment').forEach(el => {
                    el.style.display = 'block';
                });
            });
    } else {
        container.style.display = 'none';
    }
