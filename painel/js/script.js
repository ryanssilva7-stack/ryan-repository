// DOM
const horas = document.querySelector('#horas')
const minutos = document.querySelector('#minutos')
const segundos = document.querySelector('#segundos')
const dia = document.querySelector('#dia')
const dia_sep = document.querySelector('#dia_sep')
const mes = document.querySelector('#mes')
const mes_sep = document.querySelector('#mes_sep')
const ano = document.querySelector('#ano')
const ano_sep = document.querySelector('#ano_sep')
const mensagem = document.querySelector('#mensagem')

// EVENT
setInterval(relogio, 1000)

// ACTION
function relogio(){
    hoje = new Date()
    h = hoje.getHours()
    min = hoje.getMinutes()
    s = hoje.getSeconds()
    d = hoje.getDate()
    m = hoje.getMonth() + 1
    a = hoje.getFullYear()
    // msg = string

    if(h < 10){
        h ='0'+ h
    }
    if(min < 10){
        min ='0'+ min
    }
    if(m < 10){
        m ='0'+ m
    }
    if(s < 10){
        s ='0'+ s
    }
    if(d < 10){
        d ='0'+ d
    }

    if(h<12){
        msg = "BOM DIA!" 
    }

    else if(h>=12 && h<18){
        msg = "BOA TARDE!"
    }

    else if(h>=18){
    msg = "BOA NOITE!"
    }

    horas.textContent = h
    minutos.textContent = min
    segundos.textContent = s
    dia.textContent = d
    dia_sep.textContent = d
    mes.textContent = m
    mes_sep.textContent = m
    ano.textContent = a
    ano_sep.textContent = a
    mensagem.textContent = msg

}
