

window.onload = function getRequests() {

    // populating table

    $.get("/view_past_requests", function(result) {
        console.log(result);
        var arr = result["data"];
        if(arr !== 'None') {
            let table = document.querySelector('table');
            let tbody = document.querySelector('tbody');
            for(var i = 0; i < arr.length; ++i) {
                var row = `<tr data-value=${arr[i]["id"]}>`;
                row += `<th scope="row">${table.rows.length}</th>`;
                row += `<td>${arr[i]["reason"]}</td>`;
                row += `<td>${arr[i]["status"]}</td>`;
                row += '</tr>';
                tbody.innerHTML += row;
            }
        }
    });
}