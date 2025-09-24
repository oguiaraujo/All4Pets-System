
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