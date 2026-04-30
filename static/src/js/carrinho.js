

const abrirFecharCarrinho = () => {
    const carrinho = document.getElementById('secao-carrinho');
    console.log(carrinho.classList)
    const btnFechar = document.getElementById('fechar');
    const btnAbrir = document.getElementById('cart');
    

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
    dados.forEach((dado) => {
        let linha = `
         <div style="width: 100%;" class="cart-item" >
                <div class="cart-item__info">
                    <p class="cart-item__name">${dado.produto}</p>
                    <p class="cart-item__price">R$ ${dado.preco}</p>
                </div>
                <button id="${dado.codigo_itens_carrinho}" class="cart-item__remove">
                    <span class="material-symbols-outlined">delete</span>
                </button>
            </div>
        `;
        carrinho.innerHTML += linha;
        

    })
    
    } 
    const btnRemoverItem = document.querySelectorAll('.cart-item__remove');
    console.log(btnRemoverItem)
    btnRemoverItem.forEach((btn => {
        btn.addEventListener('click', () => {deleteItemCarrinho(btn.getAttribute('id'))})}))
};

const deleteItemCarrinho = async (id) => {
    const resposta = await fetch(`/api/delete/carrinho`, {method : 'DELETE',
        headers : {
            'Content-Type': 'application/json' // ESTA LINHA É A SOLUÇÃO DO ERRO 415
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





