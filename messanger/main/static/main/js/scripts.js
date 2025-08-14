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