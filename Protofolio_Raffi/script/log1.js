const masuk = document.querySelector('#masukin');


if (masuk) {
    if (localStorage.getItem("loginnn") == "true") {
        masuk.style.display = 'none';
        
    }else {
        masuk.style.display = 'block'
    }
}

