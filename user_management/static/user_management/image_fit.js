const fileInput = document.getElementById('fileInput');
const canvas = document.getElementById('imageCanvas');
const ctx = canvas.getContext('2d');
const fitButton = document.getElementById('fitButton');
const resetButton = document.getElementById('resetButton');
let img = new Image();
let originalWidth;
let originalHeight;

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
        img.src = event.target.result;
    };
    reader.readAsDataURL(file);
});

img.onload = () => {
    originalWidth = img.width;
    originalHeight = img.height;
    canvas.width = originalWidth;
    canvas.height = originalHeight;
    ctx.drawImage(img, 0, 0, originalWidth, originalHeight);
};

fitButton.addEventListener('click', () => {
    canvas.width = canvas.parentElement.clientWidth;
    canvas.height = canvas.parentElement.clientHeight;
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
});

resetButton.addEventListener('click', () => {
    canvas.width = originalWidth;
    canvas.height = originalHeight;
    ctx.drawImage(img, 0, 0, originalWidth, originalHeight);
});
