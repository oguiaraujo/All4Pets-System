
# Documento Lista de User Stories

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Plano de Automação - All4Pets](doc-visao.md)

---

### User Story US01 - Manter Cliente

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US01</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Permitir o gerenciamento completo do cadastro de clientes (criação, consulta, atualização e desativação).</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US01 - Manter Cliente</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">Como <em>Administrador, Funcionário ou Cliente</em>, quero <em>gerenciar o cadastro de cliente (criar, consultar, atualizar e desativar)</em>, para <em>que possamos manter as informações de contato atualizadas para agendamentos, vendas e comunicação</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF01.01, RF01.02, RF01.03, RF01.04</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve permitir o cadastro de um novo cliente com Nome, CPF, Telefone e E-mail.</li>
        <li>O sistema não deve permitir o cadastro de um cliente com um CPF já existente.</li>
        <li>O sistema deve exibir uma mensagem de sucesso após o cadastro/atualização de um cliente.</li>
        <li>O sistema deve validar que os campos obrigatórios (Nome, CPF, Telefone, E-mail) foram preenchidos.</li>
        <li>O sistema deve permitir a busca de clientes por Nome ou CPF.</li>
        <li>O sistema deve permitir a desativação de um cliente, que não deve mais aparecer nas buscas principais.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>TA01.01:</strong> Cadastrar um novo cliente com dados válidos e verificar se ele é salvo e uma mensagem de sucesso é exibida.</li>
        <li><strong>TA01.02:</strong> Tentar cadastrar um cliente sem preencher o campo 'Nome' e verificar se uma mensagem de erro é exibida.</li>
        <li><strong>TA01.03:</strong> Tentar cadastrar um cliente com um CPF já existente e verificar se o sistema impede a duplicidade.</li>
        <li><strong>TA01.04:</strong> Acessar a listagem de clientes e buscar por um cliente específico pelo nome.</li>
        <li><strong>TA01.05:</strong> Selecionar um cliente, editar seu número de telefone, salvar e verificar se a alteração foi persistida.</li>
        <li><strong>TA01.06:</strong> Desativar um cliente, confirmar a ação e verificar se ele não aparece mais na listagem principal de clientes.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">12 Horas</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">6 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Guilherme</li>
        <li><strong>Desenvolvedor:</strong> Guilherme</li>
        <li><strong>Revisor:</strong> Kaio</li>
        <li><strong>Testador:</strong> Samuel</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
      
    </td>
  </tr>
</table>

---

### User Story US02 - Manter Pet

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US02</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Permitir o gerenciamento do cadastro de pets, vinculando-os a um cliente.</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US02 - Manter Pet</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">Como <em>Cliente ou Funcionário</em>, quero <em>cadastrar e gerenciar as informações dos meus pets (ou dos pets de um cliente)</em>, para <em>que o histórico de saúde e agendamentos de cada animal esteja sempre correto e acessível</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF02.01, RF02.02, RF02.03, RF02.04</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve permitir o cadastro de um novo pet, que deve ser obrigatoriamente associado a um cliente existente.</li>
        <li>O sistema deve validar que os campos obrigatórios (Nome, Espécie, Nascimento) foram preenchidos.</li>
        <li>O sistema deve exibir a lista de pets ao se acessar o perfil de um cliente.</li>
        <li>O sistema deve permitir a edição e a desativação de um perfil de pet.</li>
        <li>O histórico de um pet desativado deve ser preservado e continuar acessível através de relatórios ou de uma área de "inativos".</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>TA02.01:</strong> Acessar um perfil de cliente, adicionar um novo pet com dados válidos e verificar se ele é salvo e exibido na lista de pets do cliente.</li>
        <li><strong>TA02.02:</strong> Tentar cadastrar um pet sem informar a Espécie e Nascimento e verificar se uma mensagem de erro apropriada é exibida.</li>
        <li><strong>TA02.03:</strong> Acessar o perfil de um cliente que possui 3 pets e verificar se os 3 são listados corretamente.</li>
        <li><strong>TA02.04:</strong> Selecionar um pet, editar sua Data de Nascimento, salvar e verificar se a informação foi atualizada.</li>
        <li><strong>TA02.05:</strong> Desativar o perfil de um pet, confirmar a ação e verificar se ele não é mais exibido na lista de pets ativos do cliente.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">10 Horas</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">5 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Guilherme</li>
        <li><strong>Desenvolvedor:</strong> Guilherme</li>
        <li><strong>Revisor:</strong> Kaio</li>
        <li><strong>Testador:</strong> Samuel</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
      
    </td>
  </tr>
</table>

---

### User Story US03 - Manter Funcionário

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US03</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Permitir o gerenciamento completo do cadastro de funcionários e seus perfis de acesso.</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US03 - Manter Funcionário</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">Como <em>Administrador</em>, quero <em>gerenciar os funcionários da clínica</em>, para <em>manter o quadro de pessoal atualizado e controlar o acesso ao sistema</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF03.01, RF03.02, RF03.03, RF03.04</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve permitir o cadastro de um novo funcionário com Nome, Cargo/Função, E-mail e Senha.</li>
<li>O sistema não deve permitir o cadastro de funcionários com o mesmo E-mail.</li>
        <li>O sistema deve exibir uma lista de todos os funcionários ativos e seus respectivos cargos.</li>
        <li>O sistema deve permitir a edição das informações de um funcionário, incluindo seu cargo e a redefinição de senha.</li>
        <li>O sistema deve permitir a desativação de um funcionário, o que deve revogar seu acesso ao sistema.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>TA03.01:</strong> Inserir um novo funcionário com dados válidos e verificar se ele aparece na listagem.</li>
        <li><strong>TA03.02:</strong> Tentar inserir um funcionário com um e-mail já existente e verificar se o sistema exibe uma mensagem de erro.</li>
        <li><strong>TA03.03:</strong> Atualizar o cargo de um funcionário existente, salvar e confirmar a alteração na listagem.</li>
        <li><strong>TA03.04:</strong> Desativar um funcionário e tentar fazer login com suas credenciais, verificando se o acesso é negado.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">10 Horas</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">5 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Kaio</li>
        <li><strong>Desenvolvedor:</strong> Kaio</li>
        <li><strong>Revisor:</strong> Guilherme</li>
        <li><strong>Testador:</strong> Samuel</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
    </td>
  </tr>
</table>



---

### User Story US04 - Manter Produto

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US04</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Gerenciar produtos e estoque</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US04 - Gerenciar Produtos</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">
      Como <em>Funcionário ou Administrador</em>, quero <em>cadastrar, editar e remover produtos no estoque</em>, para <em>manter o controle do inventário e evitar a falta de itens essenciais</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF04.01, RF04.02, RF04.03, RF04.04</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve permitir o cadastro de novos produtos com nome, descrição, quantidade e preço.</li>
        <li>O sistema deve permitir a edição de informações de produtos existentes.</li>
        <li>O sistema deve permitir a remoção de produtos do estoque.</li>
        <li>O sistema deve exibir uma mensagem de sucesso após cada operação.</li>
        <li>O sistema deve validar campos obrigatórios e exibir mensagens de erro.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>TA04.01 - Cadastro bem-sucedido com todos os dados preenchidos.</li>
        <li>TA04.02 - Tentativa de cadastro com campos vazios retorna erro.</li>
        <li>TA04.03 - Editar um produto existente com sucesso.</li>
        <li>TA04.04 - Excluir um produto e verificar que ele não está mais no sistema.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">12h</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">6 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Samuel</li>
        <li><strong>Desenvolvedor:</strong> Samuel</li>
        <li><strong>Revisor:</strong> Kaio</li>
        <li><strong>Testador:</strong> Guilherme</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
    </td>
  </tr>
</table>

---

### User Story US05 - Manter Serviço

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US05</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Permitir o gerenciamento do cadastro de serviços oferecidos pela clínica.</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US05 - Manter Serviço</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">Como <em>Administrador</em>, quero <em>gerenciar os serviços oferecidos pela clínica</em>, para <em>controlar a oferta de procedimentos e manter as informações de preço e duração atualizadas</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF05.01, RF05.02, RF05.03, RF05.04</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve permitir o cadastro de um novo serviço com Nome, Descrição, Preço e Duração Estimada.</li>
        <li>O sistema deve exibir uma lista com todos os serviços ativos.</li>
        <li>O sistema deve permitir a edição de todas as informações de um serviço existente.</li>
        <li>Ao desativar um serviço, ele não deve mais aparecer como uma opção para novos agendamentos.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>TA05.01:</strong> Inserir um novo serviço com dados válidos e verificar se ele aparece na listagem.</li>
        <li><strong>TA05.02:</strong> Tentar inserir um serviço sem informar o Preço e verificar se o sistema exibe uma mensagem de erro.</li>
        <li><strong>TA05.03:</strong> Atualizar o preço de um serviço e confirmar se o novo valor é refletido na listagem e na tela de agendamento.</li>
        <li><strong>TA05.04:</strong> Desativar um serviço e verificar se ele não está mais disponível para novos agendamentos.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">12 Horas</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">6 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Kaio</li>
        <li><strong>Desenvolvedor:</strong> Kaio</li>
        <li><strong>Revisor:</strong> Guilherme</li>
        <li><strong>Testador:</strong> Samuel</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
    </td>
  </tr>
</table>

---

### User Story US06 - Manter Agendamento

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US06</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Gerenciar agendamentos de serviços</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US06 - Agendamento</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">
      Como <em>Cliente ou Funcionário</em>, quero <em>agendar e cancelar serviços de banho e tosa e consultas pelo sistema</em>, para <em>ter mais conveniência e receber lembretes automáticos</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF06.01, RF06.01, RF06.01, RF06.01</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve permitir a visualização de horários disponíveis.</li>
        <li>O sistema deve permitir agendamento de serviços, selecionando data e horário.</li>
        <li>O sistema deve enviar confirmação e lembretes de agendamento.</li>
        <li>O sistema deve permitir o cancelamento do agendamento.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>TA06.01 - Agendar um serviço com sucesso.</li>
        <li>TA06.02 - O sistema envia e-mail/notificação de confirmação.</li>
        <li>TA06.03 - Cancelar um agendamento e verificar que ele foi removido do calendário.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">10h</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">5 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Samuel</li>
        <li><strong>Desenvolvedor:</strong> Samuel</li>
        <li><strong>Revisor:</strong> Guilherme</li>
        <li><strong>Testador:</strong> Kaio</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
    </td>
  </tr>
</table>

---

### User Story US07 - Realizar Venda

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US07</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Permitir o registro de vendas de produtos e serviços no ponto de venda (PDV).</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US07 - Realizar Venda</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">Como <em>Funcionário</em>, quero <em>registrar vendas de produtos e serviços e processar pagamentos</em>, para <em>manter o controle financeiro da clínica e o estoque de produtos atualizado</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF07.01, RF07.02, RF07.03, RF07.04</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve permitir a criação de uma nova venda, adicionando produtos e serviços a ela.</li>
<li>Ao finalizar uma venda, o sistema deve atualizar a quantidade em estoque dos produtos vendidos.</li>
        <li>O sistema deve permitir o registro de pagamentos para uma venda, suportando diferentes métodos (Pix, Cartão, Dinheiro).</li>
<li>O sistema deve exibir o histórico de vendas, com opções de filtro por data e cliente.</li>
        <li>O sistema deve permitir o cancelamento de uma venda não finalizada, revertendo a movimentação de estoque.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>TA07.01:</strong> Registrar uma venda com 2 produtos, processar o pagamento com Pix e verificar se a baixa no estoque foi realizada corretamente.</li>
        <li><strong>TA07.02:</strong> Acessar o histórico de vendas, filtrar por um cliente específico e verificar se todas as suas compras são exibidas.</li>
        <li><strong>TA07.03:</strong> Iniciar uma venda, adicionar 1 produto e, antes de finalizar, cancelar a operação, verificando se o estoque do produto não foi alterado.</li>
        <li><strong>TA07.04:</strong> Registrar a venda de um serviço (sem produto) e processar o pagamento com cartão, verificando se a transação é registrada no histórico.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">12 Horas</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">6 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Samuel</li>
        <li><strong>Desenvolvedor:</strong> Samuel</li>
        <li><strong>Revisor:</strong> Guilherme</li>
        <li><strong>Testador:</strong> Kaio</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
    </td>
  </tr>
</table>

---

### User Story US08 - Autenticação de Usuário

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US08</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Permitir que usuários acessem o sistema de forma segura e encerrem suas sessões.</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US08 - Autenticação de Usuário</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">Como <em>um Usuário cadastrado (Administrador, Funcionário ou Cliente)</em>, quero <em>acessar o sistema de forma segura informando minhas credenciais</em>, para <em>que eu possa ter acesso às funcionalidades correspondentes ao meu perfil e proteger minhas informações</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF08.01, RF08.02</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve fornecer uma tela de login com campos para e-mail e senha.</li>
        <li>Ao submeter credenciais válidas, o usuário deve ser autenticado e redirecionado para sua página inicial correspondente.</li>
        <li>Ao submeter credenciais inválidas, o sistema deve exibir uma mensagem de erro clara, sem especificar se o erro foi no e-mail ou na senha.</li>
        <li>Páginas restritas do sistema não devem ser acessíveis por usuários não autenticados.</li>
        <li>Um usuário autenticado deve ter acesso a um botão/link para "Sair" (Logout).</li>
<li>Ao fazer logout, a sessão do usuário deve ser encerrada e ele deve ser redirecionado para a página de login.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>TA08.01:</strong> Informar um e-mail e senha válidos e verificar se o login é bem-sucedido e o usuário é redirecionado para a página principal do seu perfil.</li>
        <li><strong>TA08.02:</strong> Informar um e-mail válido com uma senha incorreta e verificar se a mensagem "E-mail ou senha inválidos" é exibida.</li>
        <li><strong>TA08.03:</strong> Tentar acessar uma URL protegida (ex: /dashboard) sem estar logado e verificar se o sistema redireciona para a página de login.</li>
        <li><strong>TA08.04:</strong> Realizar o login, clicar no botão "Sair" e verificar se o usuário é deslogado e redirecionado para a página de login.</li>
        <li><strong>TA08.05:</strong> Após fazer logout, tentar usar o botão "Voltar" do navegador para acessar uma página interna e verificar se o acesso é bloqueado.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">6 Horas</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">3 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Guilherme</li>
        <li><strong>Desenvolvedor:</strong> Guilherme</li>
        <li><strong>Revisor:</strong> Samuel</li>
        <li><strong>Testador:</strong> Kaio</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
      
    </td>
  </tr>
</table>

---

### User Story US09 - Gerar Relatórios

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US09</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Gerar relatórios financeiros e de gestão</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US09 - Gerar Relatórios</td>
    </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">
      Como <em>Administrador</em>, quero <em>gerar relatórios financeiros e de gestão</em>, para <em>tomar decisões estratégicas e acompanhar a saúde financeira do negócio</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF09.01, RF09.02, RF09.03, RF09.04</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve permitir a geração de relatórios de vendas por período.</li>
        <li>O sistema deve permitir a geração de relatórios de estoque.</li>
        <li>O sistema deve permitir a geração de relatórios de agendamentos.</li>
        <li>Os relatórios devem ser exportáveis para formatos como PDF ou planilha.</li>
        <li>O sistema deve exibir gráficos e tabelas para facilitar a visualização dos dados.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>TA09.01 - Gerar um relatório de vendas do último mês e verificar os totais.</li>
        <li>TA09.02 - Gerar um relatório de estoque para identificar produtos com baixa quantidade.</li>
        <li>TA09.03 - Exportar um relatório de agendamentos em formato PDF.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">12h</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">6 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Importante</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Kaio</li>
        <li><strong>Desenvolvedor:</strong> Kaio</li>
        <li><strong>Revisor:</strong> Samuel</li>
        <li><strong>Testador:</strong> Guilherme</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
    </td>
  </tr>
</table>

---