
# Documento Lista de User Stories

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Plano de Automação - All4Pets](doc-visao.md)

### User Story USXX - ________

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - USXX</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Descrever funcionalidade resumidamente</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">USXX - Nome Curto</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">
      Como <em>[tipo de usuário]</em>, quero <em>[ação desejada]</em>, para <em>[benefício/valor]</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF01, RF02...</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve exibir mensagem de sucesso após cadastro correto.</li>
        <li>O sistema deve validar campos obrigatórios e exibir mensagens de erro.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>TA01.01 - Cadastro bem-sucedido com todos os dados preenchidos.</li>
        <li>TA01.02 - Tentativa com campos vazios retorna erro.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">5h</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;">2h</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;">8 PF</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial / Importante / Opcional</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Nome</li>
        <li><strong>Desenvolvedor:</strong> Nome</li>
        <li><strong>Revisor:</strong> Nome</li>
        <li><strong>Testador:</strong> Nome</li>
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

-----

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
    <td style="padding:6px;">13 PF</td>
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

-----

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
    <td style="padding:6px;">12 PF</td>
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