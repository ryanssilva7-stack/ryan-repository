// DOM
const horas = document.querySelector('#horas')
const minutos = document.querySelector('#minutos')
const segundos = document.querySelector('#segundos')

// EVENT
setInterval(relogio, 1000)

// ACTION
function relogio(){
    hoje = new Date()
    h = hoje.getHours()
    m = hoje.getMinutes()
    s = hoje.getSeconds()

    if(h < 10){
        h ='0'+ h
    }
    if(m < 10){
        m ='0'+ m
    }
    if(s < 10){
        s ='0'+ s
    }

    horas.textContent = h
    minutos.textContent = m
    segundos.textContent = s

}
