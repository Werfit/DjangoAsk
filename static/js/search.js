$(document).on('submit', '#user-search-form', e => {
    e.preventDefault()

    const form = $(e.target)

    $.ajax({
        url: form.attr('action'),
        data: form.serialize(),
        type: form.attr('method'),
        dataType: 'json',
        success: data => {
            $('#users-result-table').html(data['html'])
        },
        error: err => {
            console.error(err)
        }
    })
})