const sendBtn = document.getElementById('send-btn');
console.log("blnkjn");
sendBtn.addEventListener("click", function(e) {
    e.preventDefault();
    console.log("here1");
    const reason = document.getElementById('leave-reason').value;
    args = {'leave_reason': reason.value};
    console.log('hero');
    $.post('/send_request', args, function(resp) {
        status = resp['status']
        if(status == true) {
            reason.value = "";
        } else {
            alert("action failed");
        }
    });
});