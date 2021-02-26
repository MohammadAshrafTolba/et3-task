

const loginBtn = document.getElementById("login-btn");
loginBtn.addEventListener("click", function(e) {
    //e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const args = {'email': email, 'password': password};
    $.post('/check_credentials', args, function(resp) {
        if(resp['status'] == 'false') {
            alert("Check your credentials and try again");
        } else {
            window.location.replace("/home");
        }
    });
});
