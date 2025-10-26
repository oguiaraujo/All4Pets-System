function initActiveProductsPage(csrfToken) {
    const isAdmin = typeof IS_ADMIN !== 'undefined' && IS_ADMIN;
    const tabela = document.querySelector("#produtosTable tbody");
    const filtro = document.querySelector("#filterInput");

    if (!tabela) return; 

    const renderizarProdutos = (produtos) => {
        tabela.innerHTML = "";

        produtos.forEach(produto => {
            const tr = document.createElement("tr");

            const precoNumerico = parseFloat(produto.preco) || 0;
            const estoqueNumerico = produto.estoque || 0;
            
            let acoesHtml = '';
            let acoesTd = '';
            
            if (isAdmin) {
                acoesHtml = `
                    <a class="btn btn-edit" href="/products/edit/${produto.id}/">Editar</a>
                    <button class="btn btn-danger" onclick="desativarProduto(${produto.id})">Desativar</button>
                `;
                acoesTd = `<td>${acoesHtml}</td>`;
            }
            
            tr.innerHTML = `
                <td>${produto.codigo}</td>
                <td>${produto.nome}</td>
                <td>R$ ${precoNumerico.toFixed(2)}</td>
                <td>${estoqueNumerico}</td>
                <td>${produto.data_validade}</td>
                ${acoesTd}
            `;
            tabela.appendChild(tr);
        });
    }

    async function carregarProdutos() {
        const cacheBuster = new Date().getTime();
        const response = await fetch(`/api/products/?timestamp=${cacheBuster}`);

            if (!response.ok) {
            console.error("Erro ao carregar produtos. Status:", response.status);
            tabela.innerHTML = '<tr><td colspan="5">Não foi possível carregar a lista de produtos.</td></tr>'; 
            return;
            }

        const produtos = await response.json();
        renderizarProdutos(produtos);
    }

    if (filtro) {
        filtro.addEventListener("input", async () => {
            const nome = filtro.value.trim();
            
            if (nome.length > 0) {
                const response = await fetch(`/api/products/?search=${encodeURIComponent(nome)}`);
                if (!response.ok) {
                    console.error("Erro na busca por produtos. Status:", response.status);
                    tabela.innerHTML = '<tr><td colspan="5">Erro ao buscar.</td></tr>';
                    return;
                }

                const produtos = await response.json();
                renderizarProdutos(produtos);
            } else {
                carregarProdutos();
            }
        });
    }

    window.desativarProduto = async (id) => {
        if (confirm("Deseja realmente desativar este produto?")) {
            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
            const response = await fetch(`/api/products/${id}/`, {
                method: "PATCH",
                headers: { 
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken 
                },
                body: JSON.stringify({ ativo: false })
            });
        
            if (!response.ok) {
                alert("Erro ao desativar produto.");
            }
        
            carregarProdutos();
        }
    };

    carregarProdutos(); 
}

function initInactiveProductsPage(csrfToken) {
    const tabelaBody = document.querySelector("#inactiveProductsTable tbody");
    const reactivateBtn = document.querySelector("#reactivateButton");
    const selectAllCheckbox = document.querySelector("#selectAllCheckbox");

    if (!tabelaBody || !reactivateBtn || !selectAllCheckbox) return;

    const renderizarProdutos = (produtos) => {
        tabelaBody.innerHTML = "";
        if (!produtos || produtos.length === 0) {
             tabelaBody.innerHTML = '<tr><td colspan="5" class="text-center">Nenhum produto inativo encontrado.</td></tr>';
             reactivateBtn.disabled = true;
             return;
        }
        
        reactivateBtn.disabled = false;
        produtos.forEach(produto => {
            const tr = document.createElement("tr");
            const precoNumerico = parseFloat(produto.preco) || 0;
            const estoqueNumerico = produto.estoque || 0;
            
            tr.innerHTML = `
                <td class="text-center"><input type="checkbox" class="product-checkbox" value="${produto.id}"></td>
                <td>${produto.codigo}</td>
                <td>${produto.nome}</td>
                <td>R$ ${precoNumerico.toFixed(2)}</td>
                <td>${estoqueNumerico}</td>
                <td>${produto.data_validade}</td>
                <td>${produto.ativo ? "Ativo" : "Inativo"}</td>
            `;
            tabelaBody.appendChild(tr);
        });
    }

    async function carregarProdutosInativos() {
        tabelaBody.innerHTML = '<tr><td colspan="5" class="text-center">Carregando...</td></tr>';
        
        const cacheBuster = new Date().getTime();
        const response = await fetch(`/api/products/?ativo=false&timestamp=${cacheBuster}`);

        if (!response.ok) {
            console.error("Erro ao carregar produtos inativos:", response.status);
            tabelaBody.innerHTML = '<tr><td colspan="5" class="text-center text-danger">Falha ao carregar.</td></tr>';
            return;
        }

        const produtos = await response.json();
        renderizarProdutos(produtos);
    }

    async function reativarProdutos(ids) {
        if (!confirm(`Deseja realmente reativar ${ids.length} produto(s)?`)) {
            return;
        }
        
        reactivateBtn.disabled = true;
        reactivateBtn.textContent = "Reativando...";
        const requests = ids.map(id => {
            return fetch(`/api/products/${id}/`, {
                method: "PATCH",
                headers: { 
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken 
                },
                body: JSON.stringify({ ativo: true })
            });
        });

        try {
            const responses = await Promise.all(requests);
            const falhas = responses.filter(res => !res.ok);
            
            if (falhas.length > 0) {
                alert(`Erro ao reativar ${falhas.length} produto(s).`);
                console.error("Falhas na reativação:", falhas);
            } else {
                alert(`Sucesso! ${ids.length} produto(s) foram reativados.`);
            }

        } catch (error) {
            alert("Ocorreu um erro geral.");
            console.error("Erro em Promise.all:", error);
        }
        reactivateBtn.disabled = false;
        reactivateBtn.textContent = "Reativar Selecionados";
        carregarProdutosInativos();
    }

    reactivateBtn.addEventListener("click", () => {
        const checkboxes = document.querySelectorAll(".product-checkbox:checked");
        const idsParaReativar = Array.from(checkboxes).map(cb => cb.value);
        if (idsParaReativar.length === 0) {
            alert("Por favor, selecione pelo menos um produto para reativar.");
            return;
        }

        reativarProdutos(idsParaReativar);
    });

    selectAllCheckbox.addEventListener("click", () => {
        const checkboxes = document.querySelectorAll(".product-checkbox");
        checkboxes.forEach(cb => {
            cb.checked = selectAllCheckbox.checked;
        });
    });

    carregarProdutosInativos();
}

document.addEventListener("DOMContentLoaded", () => {
    
    const csrfTokenEl = document.querySelector('meta[name="csrf-token"]');
    if (!csrfTokenEl) {
        console.error("A meta tag 'csrf-token' não foi encontrada.");
        return;
    }
    const csrfToken = csrfTokenEl.getAttribute('content');

    const activeTable = document.querySelector("#produtosTable");
    const inactiveTable = document.querySelector("#inactiveProductsTable");

    if (activeTable) {
        initActiveProductsPage(csrfToken);
    } else if (inactiveTable) {
        initInactiveProductsPage(csrfToken);
    }
});