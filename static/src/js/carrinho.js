

const abrirFecharCarrinho = () => {
    const carrinho = document.getElementById('secao-carrinho');
    const btnFechar = document.getElementById('fechar');
    const btnAbrir = document.getElementById('cart');
    
if (carrinho){
    // Função para abrir
btnAbrir.addEventListener('click', () => {
    console.log(carrinho)
    carrinho.classList.add('carrinho-aberto');
    carregarCarrinho()

});

// Função para fechar
btnFechar.addEventListener('click', () => {
    carrinho.classList.remove('carrinho-aberto');
});
}
}

abrirFecharCarrinho()

const carregarCarrinho = async () => {

    const resposta = await fetch('/api/get/carrinho');

    if (!resposta.ok){
        alert('ERRO AO CARREGAR CARRINHO');
    }
   else {
    const dados = await resposta.json();
    
    const carrinho = document.getElementById('carrinho');

    carrinho.innerHTML = '';
    const precoTotal = document.querySelector('.cart-total__value')
    valorTotal = 0
    dados.forEach((dado) => {
        let linha = `
         <div style="width: 100%;" class="cart-item" >
                <div class="cart-item__info">
                    <p class="cart-item__name">${dado.produto}</p>
                    <p class="cart-item__price">R$ ${dado.preco}</p>
                    <p class="cart-item__price">Quantidade: ${dado.quantidade}</p>
                </div>
                <button id="${dado.codigo_itens_carrinho}" class="cart-item__remove">
                    <span class="material-symbols-outlined">delete</span>
                </button>
            </div>
        `;
        valorTotal += parseInt(dado.preco * dado.quantidade)
        console.log(valorTotal)
        carrinho.innerHTML += linha;
    })
    precoTotal.textContent = `R$ ${valorTotal.toFixed(2)}`

    console.log(precoTotal)
    } 
    const btnRemoverItem = document.querySelectorAll('.cart-item__remove');
    console.log(btnRemoverItem)
    btnRemoverItem.forEach((btn => {
        btn.addEventListener('click', () => {deleteItemCarrinho(btn.getAttribute('id'))})}))
};

const deleteItemCarrinho = async (id) => {
    const resposta = await fetch(`/api/delete/carrinho`, {method : 'DELETE',
        headers : {
            'Content-Type': 'application/json'
        },
        body : JSON.stringify({codigo : id})
    });
    
    if (!resposta.ok){
        alert('Erro na hora de Deletar pai')
    }
    else {
        carregarCarrinho()
        
    }
}



const adicionarItemCarrinho = async (codigo_produto = 1) => {
    const quantidade = document.querySelector('.qty-input').value
    const resposta = await fetch(`/api/post/carrinho`, {method : 'POST',
        headers : {
            'Content-Type': 'application/json'},
        body : JSON.stringify({codigo_produto : codigo_produto,
                            quantidade : quantidade})
                        })
         if (!resposta.ok){
        alert('Erro na hora de Inserir pai')
    }

}




// async function adicionarAoCarrinho(codigoProduto) {
//     const dados = {
//         codigo: codigoProduto,
//         quantidade: 1
//     };

//     const response = await fetch('/api/post/carrinho', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(dados) // Converte o objeto JS para uma string JSON
//     });

//     const resultado = await response.json();

//     if (response.ok) {
//         alert("Produto adicionado ao carrinho!");
//     } else {
//         alert("Erro: " + resultado.message);
//     }
// }
