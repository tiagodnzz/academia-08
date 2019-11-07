let caractere = prompt("Digite o caractere desejado");

let quantidade = Number(prompt("Digite a quantidade de degrais da escada"))

let valoratual = caractere;

for (let i = 0; i < quantidade; i++) {
    if (i==0) {
        console.log(caractere)
    }else{
        console.log(caractere+=valoratual)
    }
}