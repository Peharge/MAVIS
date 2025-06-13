const textarea = document.getElementById('message-text');
const input = document.getElementById('message');
const sendButton = document.getElementById('send-button');

textarea.addEventListener('input', () => {
    input.value = textarea.value;
});

sendButton.addEventListener('click', () => {
    textarea.value = input.value;
    input.value = textarea.value;
    alert(`Message sent: ${input.value}`);
});