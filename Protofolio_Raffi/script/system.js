const sc = document.getElementById('pembesar');
const app = document.getElementById('app');
const show = document.getElementById('show');
const j = document.getElementById('j');
const apa = document.getElementById('apa');

const all = document.getElementById('tomb1');
const horror = document.getElementById('tomb2');
const adventure = document.getElementById('tomb3');
const puzzle = document.getElementById('tomb4');
const action = document.getElementById('tomb5')


const tema1 = document.getElementById('all');
const tema2 = document.getElementById('horror');
const tema3 = document.getElementById('adventure');
const tema4 = document.getElementById('puzzle');
const tema5 = document.getElementById('action');


let ubah = false;


if (sc) {
    sc.addEventListener('click', () => {
    
    app.classList.toggle('sembunyi');
    show.classList.toggle('sembunyi');
    j.classList.toggle('sembunyi');
    apa.classList.toggle('sembunyi');


}
);

}


if (all) {
    all.addEventListener('click', () => {
   
    tema1.style.display = 'block';
    tema2.style.display = 'none';
    tema3.style.display = 'none';
    tema4.style.display = 'none';
    tema5.style.display = 'none';

    all.classList.add('active');

    horror.classList.remove('active');
    adventure.classList.remove('active');
    puzzle.classList.remove('active');
    action.classList.remove('active');

}

);

}


if (horror) {
    horror.addEventListener('click', () => {
   
    tema1.style.display = 'none';
    tema2.style.display = 'block';
    tema3.style.display = 'none';
    tema4.style.display = 'none';
    tema5.style.display = 'none';

    all.classList.remove('active');
    adventure.classList.remove('active');
    puzzle.classList.remove('active');
    action.classList.remove('active');

    horror.classList.add('active');
}

);

}


if (adventure) {
    adventure.addEventListener('click', () => {
   
    tema1.style.display = 'none';
    tema2.style.display = 'none';
    tema3.style.display = 'block';
    tema4.style.display = 'none';
    tema5.style.display = 'none';
    
    all.classList.remove('active');
    horror.classList.remove('active');
    puzzle.classList.remove('active');
    action.classList.remove('active');
    adventure.classList.add('active');
}

);

}


if (puzzle) {
    puzzle.addEventListener('click', () => {
   
    tema1.style.display = 'none';
    tema2.style.display = 'none';
    tema3.style.display = 'none';
    tema4.style.display = 'block';
    tema5.style.display = 'none';
    action.classList.remove('active');
    all.classList.remove('active');
    horror.classList.remove('active');
    adventure.classList.remove('active');
    puzzle.classList.add('active');
}

);


}


if (action) {
    action.addEventListener('click', () => {
   
    tema1.style.display = 'none';
    tema2.style.display = 'none';
    tema3.style.display = 'none';
    tema4.style.display = 'none';
    tema5.style.display = 'block';

    all.classList.remove('active');
    horror.classList.remove('active');
    adventure.classList.remove('active');
    puzzle.classList.remove('active');
    action.classList.add('active');
}

);

}




