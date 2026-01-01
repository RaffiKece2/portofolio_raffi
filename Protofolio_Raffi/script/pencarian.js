


const cari = document.getElementById('cari');
const input = document.getElementById('pembesar');
const item = document.querySelectorAll('.judul1');


let pindah = false;

cari.addEventListener( 'click',() => {

    if (!pindah) {
        cari.style.right = '300px';
        input.style.opacity = '1';
        input.style.visibility = 'visible';
        
        pindah = true;
    }else {
        cari.style.right = '100px';
        input.style.opacity = '0';
        input.style.visibility = 'hidden';
        pindah = false;
    }



}
);
