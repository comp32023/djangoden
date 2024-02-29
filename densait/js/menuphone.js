let menu = document.querySelector(".menumobkart");
let content = document.querySelector(".contentmobile");
let zakrivashka = document.querySelector(".knmobile2");


menu.addEventListener('click', function(){
    content.setAttribute('id',"otcritiy");
    content.style.display = null;
    content.style.display = 'square';
})

zakrivashka.addEventListener('click', function(){
    content.style.display = null;
    content.style.display = 'none';
})