document.getElementById("send-form").onsubmit = async function(event) {
    event.preventDefault();

    const message = document.getElementById("message").value;
    const image = document.getElementById("image").files[0];

    const formData = new FormData();
    formData.append('message', message);
    formData.append('image', image);

    const chatContent = document.getElementById("chat-content");
    const loadingIndicator = document.getElementById("loading");

    loadingIndicator.style.display = 'block';

    const response = await fetch("/send_message", {
        method: "POST",
        body: formData
    });

    loadingIndicator.style.display = 'none';

    const data = await response.json();
    if (data.response) {
        chatContent.innerHTML += `
            <div class="user-box">
                  <p>${message}</p>
            </div>
            <div>
                <img class="img-out-out" src="${data.image_url}" alt="Hochgeladenes Bild">
            </div>`;

        chatContent.innerHTML += `
            <div class="chatbot-box">
                <p>${data.response}</p>
            </div>`;

        chatContent.innerHTML += `
            <div class="chatbot-box-code">
                <p>${data.code}</p>
            </div>`;

        MathJax.typeset();
    } else {
        chatContent.innerHTML += `<p><strong>Fehler:</strong> ${data.error}</p>`;
    }

};

const taskBox = document.getElementById('button-containerid');

let offsetXTask, offsetYTask;

taskBox.addEventListener('mousedown', (e) => {
    offsetXTask = e.clientX - taskBox.getBoundingClientRect().left;
    offsetYTask = e.clientY - taskBox.getBoundingClientRect().top;

    document.addEventListener('mousemove', moveTaskBox);
    document.addEventListener('mouseup', stopMovingTaskBox);
});

function moveTaskBox(e) {
    taskBox.style.left = `${e.clientX - offsetXTask}px`;
    taskBox.style.top = `${e.clientY - offsetYTask}px`;
}

function stopMovingTaskBox() {
    document.removeEventListener('mousemove', moveTaskBox);
    document.removeEventListener('mouseup', stopMovingTaskBox);

    const textarea = document.querySelector('.input');

textarea.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = `${this.scrollHeight}px`;
});

}

function toggleCard() {
    const card = document.querySelector('.card');

    if (card.style.display === 'none' || card.style.display === '') {
        card.style.display = 'block';
    } else {
        card.style.display = 'none';
    }
}

function toggleCardd() {
    const cardd = document.querySelector('.cardd');

    if (cardd.style.display === 'none' || cardd.style.display === '') {
        cardd.style.display = 'block';
    } else {
        cardd.style.display = 'none';
    }
}

function toggleCarddd() {
    const carddd = document.querySelector('.carddd');

    if (carddd.style.display === 'none' || carddd.style.display === '') {
        carddd.style.display = 'block';
    } else {
        carddd.style.display = 'none';
    }
}

function toggleCardddd() {
    const cardddd = document.querySelector('.cardddd');

    if (cardddd.style.display === 'none' || cardddd.style.display === '') {
        cardddd.style.display = 'block';
    } else {
        cardddd.style.display = 'none';
    }
}

function toggleCarddddd() {
    const cardddd = document.querySelector('.carddddd');

    if (cardddd.style.display === 'none' || cardddd.style.display === '') {
        cardddd.style.display = 'block';
    } else {
        cardddd.style.display = 'none';
    }
}

document.getElementById("askInput").addEventListener("keydown", function(event) {
      if (event.key === "Enter") {
            event.preventDefault();
            loadScene();
      }
});

function previewImage(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function() {
          const preview = document.getElementById('preview');
          preview.src = reader.result;
          document.getElementById('image-preview').style.display = 'block';
    };

    if (file) {
          reader.readAsDataURL(file);
    }
}

function closePreview() {
    document.getElementById('image-preview').style.display = 'none';
}