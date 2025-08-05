let results =[]
function runSending(sending, csrfmiddlewaretoken){
$.ajaxSetup({data:{csrfmiddlewaretoken}})
$.post('/mailing/run',{sending}, function(response, status){
if(status==='success'){
    getResults(sending, csrfmiddlewaretoken)
}
},'json')
}

function getResults(sending, csrfmiddlewaretoken){
    $.ajaxSetup({data:{csrfmiddlewaretoken}})
    $.get('/mailing/results/'+sending, function(response,status){
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
        row += '<td>' + item.fields.status + '</td>'
        row += '<td>' + item.fields.response + '</td>'
        row += '</tr>'
        tableBody.append(row)
    })
}