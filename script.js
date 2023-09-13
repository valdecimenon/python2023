var ind_imagem = 1
var opacidade = 1
var reduzir = true
var id_intervalo_mover, id_intervalo_trocar

function trocar_imagem(){
    let imagem = document.getElementById('imagem')
    
    ind_imagem++
    if (ind_imagem > 7)
        ind_imagem = 1

    imagem.src = "https://softgraf.com/img/img" + ind_imagem + ".jpg"
}

function mudar_opacidade(){
    let imagem = document.getElementById('imagem')

    if (opacidade <= 0.1)
        reduzir = false
    else if (opacidade >= 1)
        reduzir = true

    if (reduzir)
        opacidade -= 0.1
    else
        opacidade += 0.1

    imagem.style.opacity = opacidade
}

// arrow function =>
const mover_imagem = () => {
    let imagem = document.getElementById('imagem')
    // tenta converter o valor da margem (string) para formato inteiro
    let margem_esq = parseInt(imagem.style.marginLeft)
    let largura_tela = window.innerWidth
    let largura_imagem = imagem.clientWidth
    
    if (Number.isNaN(margem_esq))
        margem_esq = 5  // atribui 5
    else
        margem_esq += 5 // soma 5

    if (margem_esq > largura_tela)
        margem_esq = -largura_imagem

    imagem.style.marginLeft = margem_esq + 'px'
}

const auto_mover = () => {
    id_intervalo_mover = setInterval('mover_imagem()', 20)
}

const auto_trocar = () => {
    id_intervalo_trocar = setInterval('trocar_imagem()', 1000)
}

document.addEventListener('DOMContentLoaded', () => {
    
    document.getElementById('btn_reset').onclick = () => {
        clearInterval(id_intervalo_mover)
        clearInterval(id_intervalo_trocar)
    }
})

