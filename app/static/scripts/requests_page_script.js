

window.onload = function getRequests() {

    // populating table

    $.get("/get_requests", function(result) {
        console.log(result);
        var arr = result["data"];
        if(arr !== 'None') {
            let table = document.querySelector('table');
            let tbody = document.querySelector('tbody');
            for(var i = 0; i < arr.length; ++i) {
                var row = `<tr data-value=${arr[i]["id"]}>`;
                row += `<th scope="row">${table.rows.length}</th>`;
                row += `<td>${arr[i]["employee_name"]}</td>`;
                row += `<td>${arr[i]["employee_email"]}</td>`;
                row += `<td>${arr[i]["reason"]}</td>`;
                row += '<td><button type="button" class="btn btn-success approve" value="approve">Approve</button></td>';
                row += '<td><button type="button" class="btn btn-danger decline" value="decline">Decline</button></td>';
                row += '</tr>';
                tbody.innerHTML += row;
            }

            var approveBtns = document.getElementsByClassName('approve');
            var declineBtns = document.getElementsByClassName('decline');

            for(var i = 0; i < table.rows.length-1; ++i) {
                
                approveBtns[i].addEventListener("click", function(e) {
                    e.preventDefault();
                    const row = this.parentNode.parentNode;
                    const request_id = row.dataset.value;
                    const args = {'request_id': request_id, 'action': 2};
                    $.post('/request_action', args, function(resp) {
                        if(resp['status'] == true) {
                            table.deleteRow(row.rowIndex);
                            //alert('action successful');
                        } else {
                            alert('action failed');
                        }
                    });
                });

                declineBtns[i].addEventListener("click", function(e) {
                    e.preventDefault();
                    const row = this.parentNode.parentNode;
                    const request_id = row.dataset.value;
                    const args = {'request_id': request_id, 'action': 1};
                    $.post('/request_action', args, function(resp) {
                        if(resp['status'] == true) {
                            table.deleteRow(row.rowIndex);
                            //alert('action successful');
                        } else {
                            alert('action failed');
                        }
                    });
                });
            }

        }
    });
}