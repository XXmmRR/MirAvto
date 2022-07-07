//




let body = document.body
let first = document.querySelector('.first1')
let first_flex_block_in_container = document.querySelector('.first_flex_block_in_container')
let second_header_cont = document.querySelector('.second_header_cont')
let burg_menu = document.querySelector('.burg_menu')
let width20 = document.querySelector('.width20')

width20.onclick = () => {
    body.classList.add('modal')
}

burg_menu.onclick = () => {
    first.classList.toggle('active_burg')
}


second_header_cont.onclick = () => {
    first_flex_block_in_container.classList.toggle('first_flex_active')
}




