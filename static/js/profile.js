$(document).on('submit', 'form', e => {
    e.preventDefault()

    const form = $(e.target)

    $.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: form.serialize(),
        dataType: 'json',
        success: data => {
            $('.table > tbody').html(data['html'])
        }
    })
})