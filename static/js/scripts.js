function editLabelForSignup() {
    let id = 'id_email'
    labels = document.getElementsByTagName('label');
    for (i = 0; i < labels.length; i++) {
        if (labels[i].htmlFor == id) {
            document.getElementById('id_email').label.innerHTML = 'Email:';
        }
    }
}