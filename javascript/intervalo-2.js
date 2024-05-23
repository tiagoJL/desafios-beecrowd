const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.trim().split('\n');

let quantidade_in = 0
let quantidade_out = 0

numeros_teste = lines.slice(1, lines.length)

numeros_teste.forEach(
    (numero) => {
        let numero_is_in = +numero >= 10 && +numero <= 20
        if (numero_is_in) {quantidade_in += 1}
        else {quantidade_out += 1}
    }
)

console.log(`${quantidade_in} in`)
console.log(`${quantidade_out} out`)