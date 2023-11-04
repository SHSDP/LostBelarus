var elements = document.getElementsByClassName('image')
for(var i=0;i<elements.length;i++){
    elements[i].addEventListener("click", function(event) {
        document.getElementById("modal-content").setAttribute('src', event.target.getAttribute('src'))
        document.getElementById("caption").innerHTML = event.target.getAttribute('name')
        document.getElementById("autor").textContent = 'Автор : ' +  event.target.getAttribute('autor')
        document.getElementById("sourc").textContent = 'Источник : ' +  event.target.getAttribute('sourc')
        document.getElementById("myModal").style.display = "block"
        document.body.style.overflow = "hidden"
    })
}



var close = document.getElementById("close")
close.addEventListener('click',function(){
    document.getElementById("myModal").style.display = "none";
    document.body.style.overflow = "";
})