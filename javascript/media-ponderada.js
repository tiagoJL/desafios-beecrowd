var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

for (let interator = 1; interator <= +lines[0]; interator++){
    let valores = lines[interator].split(' ')
    let primeiro_valor = +valores[0] * 2
    let segundo_valor = +valores[1] * 3
    let terceiro_valor = +valores[2] * 5
    let resultado = (primeiro_valor + segundo_valor + terceiro_valor) / 10
    console.log(resultado.toFixed(1))
}
