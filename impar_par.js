const Numeros = [2, 10, 3, 6, 7, 8]
let par = 0
let impar = 0
let neutro = 0

for (let i = 0; i <= 5; i++) {
    if (Numeros[i] == 0) {
        neutro++
    } else if (Numeros[i] % 2 == 0) {
        par++
    } else {
        impar++
    }
}
if (neutro > 0)
    console.log(`${par} são pares, ${impar} são ímpares e ${neutro} são neutros. `)
else
    console.log(`${par} são pares e ${impar} são ímpares.`)
