



const carregarCarrinho = async () => {

    const resposta = await fetch('http://10.110.134.2:8080/api/get/carrinho');

    if (!resposta.ok){
        alert('ERRO AO CARREGAR CARRINHO');
    }
   else {
    const dados = await resposta.json();
    
    const carrinho = document.getElementById('carrinho');

    carrinho.innerHTML = '';
    let precoTotal = 0
    dados.forEach((dado) => {
        let linha = `
         <div style="width: 100%;" class="cart-item" >
                <div class="cart-item__info">
                    <p class="cart-item__name">${dado.nome}</p>
                    <p class="cart-item__price">R$ ${dado.preco}</p>
                </div>
                <button class="cart-item__remove">
                    <span class="material-symbols-outlined">delete</span>
                </button>
            </div>
        `;
        carrinho.innerHTML += linha;
        

        precoTotal += dado.preco
    })
    document.querySelector('.cart-total__value').textContent = precoTotal.toFixed(2).replace('.', ',')
    } 

};

const deleteItemCarrinho = async (id) => {
    const resposta = await fetch(`http://10.110.134.2:8080/api/get/carrinho/${id}`, {method : 'DELETE'});

    if (!resposta.ok){
        alert('Erro na hora de Deletar pai')
    }
    else {
        alert('Deu bom')
        
    }
}
carregarCarrinho()







