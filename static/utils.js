function runMailing(mailing, csrfmiddlewaretoken){
$.ajaxSetup({data:{csrfmiddlewaretoken}})
$.post('/mailing/run',{mailing}, function(response, status){
if(status==='success'){
    getResults(mailing, csrfmiddlewaretoken)
}
},'json')
}

function blockUser(user, csrfmiddlewaretoken){
    $.ajaxSetup({data:{csrfmiddlewaretoken}})
    $.post('/mailing/block-user/'+user, function(response,status){
    if(status==='success'){
        window.location.reload();
        }
    })
}
function disableMailing(id, csrfmiddlewaretoken){
    $.ajaxSetup({data:{csrfmiddlewaretoken}})
    $.post('/mailing/disable-mailing/'+id, function(response,status){
    if(status==='success'){
        window.location.reload();
        }
    })
}

function getResults(mailing, csrfmiddlewaretoken){
    $.ajaxSetup({data:{csrfmiddlewaretoken}})
    $.get('/mailing/results/'+mailing, function(response,status){
        if(status==='success'){
            drawTable(response)
        }
    })
}

function drawTable(rows){
console.log(rows)
    const tableBody = $('#results-table');
    tableBody.empty();
    $.each(rows, function(index, item){
        row = '<tr>'
        row += '<td>' + item.fields.date + '</td>'
        row += '<td>' + item.fields.email + '</td>'
        row += '<td>' + item.fields.status + '</td>'
        row += '<td>' + item.fields.response + '</td>'
        row += '</tr>'
        tableBody.append(row)
    })
}