document.addEventListener('DOMContentLoaded', function() {
    var list = document.querySelectorAll('div')[0].querySelectorAll('li')

    for (i = 0; i < list.length; i++) {
        list[i].style.display = 'none'
    }
    var l = document.querySelectorAll('div')[0].querySelectorAll('.errorlist')
    if (l.length) {
        list[list.length - 1].style.display = ''
    }
    var sp = document.querySelectorAll('div')[0].querySelectorAll('span')
    for (i = 0; i < sp.length; i++) {
        sp[i].textContent = ''
    }


    var labels = document.querySelectorAll('label')
    for (i = 0; i < labels.length; i++) {
        labels[i].style.display = 'none'
    }

    var input = document.querySelectorAll('input')
    for (i = 1; i < input.length; i++) {
        input[i].placeholder = labels[i - 1].textContent
    }
    var boxlength;
    if (labels.length > 10) {
        boxlength = labels.length * 67 + 'px'
    } else {
        boxlength = labels.length * 75 + 'px'
    }

    document.querySelectorAll('div')[1].style.height = boxlength;

    var select = document.querySelector('select')
    var option = document.querySelector('option')
    option.textContent = 'School:'
    select.style.height = '30px';
    select.style.width = '300px';
    select.style.backgroundColor = '#e8ebf3';
    select.style.color = '#757575';
    select.style.textIndent = '35px';




})