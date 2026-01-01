const notif = document.querySelector('#notif');
const identitas = document.querySelector('#identitas');
const logout = document.querySelector('#keluar');
const btn3 = document.querySelector('#btn3');

if (btn3) {
    btn3.addEventListener('click',() => {
       alert('Makasihh Atas Ulasan Andaa!');

    }

    );
    
}


if (logout) {
    logout.addEventListener('click',() => {
        localStorage.setItem("loginnn","false");
        location.href = 'index.html'

    }
    
    );
}

if (localStorage.getItem("loginnn") == "true") {
    if (notif) {
        notif.style.display = 'none';
    }
    if (identitas) {
        identitas.style.display = 'block';
    }

    if (logout) {
        logout.style.display = 'block'
    }
}else {
    if (notif) {
        notif.style.display = 'block';

    }
    if (identitas) {
        identitas.style.display = 'none'
    }
    
    if (logout) {
        logout.style.display = 'none'
    }
}

