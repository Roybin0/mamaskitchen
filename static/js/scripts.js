var medium_screen = window.matchMedia("(max-width: 768px)")
var small_screen = window.matchMedia("(max-width: 576px)")

function editLabelForSignup() {
    let id = 'id_email';
    labels = document.getElementsByTagName('label');
    for (i = 0; i < labels.length; i++) {
        if (labels[i].htmlFor == id) {
            document.getElementById('id_email').label.innerHTML = 'Email:';
        }
    }
}

function changeFooter(screen_size) {
    if (screen_size.matches) { 
        footer = document.getElementById("footer"); 
        footer.classList.remove("fixed-bottom");
    } 
}
  
changeFooter(medium_screen)
