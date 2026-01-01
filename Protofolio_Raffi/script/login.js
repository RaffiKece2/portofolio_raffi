const login = document.querySelector('#login');

const logout = document.querySelector('#keluar');


if (logout) {
    logout.addEventListener('click',() => {
        localStorage.setItem("loginnn","false");

    }
    
    );
}

if (login) {
    login.addEventListener('click',() => {
        localStorage.setItem("loginnn","true");
        location.href = 'index.html';
    }

    );
}