const a = document.getElementById('bintang');
const b = document.getElementById('bintang2');
const c = document.getElementById('bintang3');
const d = document.getElementById('bintang4');
const teks = document.getElementById('pesan');
const teks2 = document.getElementById('pesan2');


const isi = document.querySelectorAll('.rivew .star .bintang1');

const ganti = [
    '25%',
    '50%',
    '75%',
    '95%'
]

const ganti2 = [
    'Bad',
    'Reasonable',
    'Good',
    'Popular'
]

let index = 0;  


a.addEventListener( 'click',() => {

    index = (index + 1) % isi.length;
    teks.textContent = ganti[index]
    isi[index].classList.add('active');
    teks2.textContent = ganti2[index]
}
);

b.addEventListener('click', () => {
 
    index = (index + 1) % isi.length;
    teks.textContent = ganti[index]
    isi[index].classList.add('active');
    teks2.textContent = ganti2[index]
}
);

c.addEventListener( 'click', () => {
  
    index = (index + 1) % isi.length;
    teks.textContent = ganti[index]
    isi[index].classList.add('active');
    teks2.textContent = ganti2[index]
}

);

d.addEventListener( 'click',() => {
 
    index = (index + 1) % isi.length;
    teks.textContent = ganti[index]
    isi[index].classList.add('active');
    teks2.textContent = ganti2[index]
}

);

