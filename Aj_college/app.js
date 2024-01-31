let burger=document.querySelector(".burger");
let links=document.querySelector(".nav_links")
let textarea=document.querySelector(".text-area")
burger.addEventListener('click',()=>{
    links.classList.toggle("nav-show")
    textarea.classList.toggle("textareahide")
})
