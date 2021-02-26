const sendBtn = document.getElementById('send-btn');
sendBtn.addEventListener("click", function(e) {
    e.preventDefault();
    var reason = document.getElementById('leave-reason');
    args = {'leave_reason': reason.value};
    $.post('/send_request', args, function(resp) {
        console.log(resp);
        const status = resp['status'];
        //console.log(status);
        if(status === 'true') {
            console.log(true);
            reason.value = "";
        } else {
            alert("action failed");
        }
    });
});