const slide = document.querySelectorAll('.scroll1 .gambar');
let index = 0;
const dots = document.querySelectorAll('.dot');

const pesan = [
    'Marvels Spiderman Remastered',
    'Uncharted Drake Deception',
    'Naruto Shippuden Ultimate Ninja Storm',
    'Minecraft'
];

const harga = [
    '100.000',
    '250.000',
    '95.000',
    '280.000'

];

const pesan1 = document.getElementById('caption');

const pesan2 = document.getElementById('caption1');

function updateSlide(newIndex, direction) {

    slide[index].classList.remove('active');
    dots[index].classList.remove('active');

    if (direction === 'next') {
        slide[index].style.left = "-100%";
    } else {
        slide[index].style.left = "100%";
    }

    index = newIndex;


    slide[index].classList.add('active');
    dots[index].classList.add('active');

    pesan1.textContent = pesan[index];
    pesan2.textContent = harga[index];
}

document.getElementById('right1').addEventListener('click', () => {
    updateSlide((index + 1) % slide.length, 'next');
});

document.getElementById('left1').addEventListener('click', () => {
    updateSlide((index - 1 + slide.length) % slide.length, 'prev');
});