## Perfis dos Usuários

O sistema poderá ser utilizado por diversos usuários. Temos os seguintes perfis/atores:

Perfil | Descrição |
--------- | ----------- |
**Administrador** | Este usuário, geralmente o gestor da clínica, realiza os cadastros base (funcionários, produtos, serviços) e tem acesso a todas as funcionalidades do sistema, incluindo relatórios financeiros e de gestão.
**Funcionário** | Este usuário (veterinário, groomer, recepcionista) realiza as operações do dia a dia, como gerenciar clientes e pets, agendar serviços, registrar vendas e pagamentos.
**Cliente** | Este usuário, o dono do pet, utiliza o sistema para agendar serviços, visualizar o histórico de seus animais, receber notificações e realizar pagamentos online.

## Lista de Requisitos Funcionais

### Entidade Cliente - US01 - Manter Cliente
Um cliente representa o dono do pet. Um cliente tem: Nome Completo, CPF, Telefone e E-mail.

Requisito | Descrição | Ator |
--------- | ----------- | ---------- |
RF01.01 - Inserir Cliente | Insere novo cliente informando: Nome, CPF, Telefone e E-mail. | Funcionário, Cliente |
RF01.02 - Listar Clientes | Listagem dos clientes utilizando filtros por Nome e CPF. | Funcionário |
RF01.03 - Atualizar Cliente | Atualiza as informações de um cliente: Nome, Telefone, E-mail e Endereço. | Funcionário, Cliente |
RF01.04 - Desativar Cliente | Desativa um cliente (exclusão lógica), mantendo seu histórico de transações. |Funcionário, Cliente |

---

### Entidade Pet - US02 - Manter Pet
Um pet é um animal de estimação que pertence a um Cliente. Um pet tem: ID, Nome, Espécie, Raça, Data de Nascimento e Observações.

Requisito | Descrição | Ator |
--------- | ----------- | ---------- |
RF02.01 - Inserir Pet | Insere novo pet informando: ID, Nome, Espécie, Raça, Data de Nascimento e Observações, associando-o a um cliente. | Cliente, Funcionário |
RF02.02 - Listar Pets | Listagem dos pets vinculados a um perfil de cliente. | Cliente, Funcionário |
RF02.03 - Atualizar Pet | Atualiza as informações de um pet. | Cliente, Funcionário |
RF02.04 - Desativar Pet | Desativa o perfil de um pet (exclusão lógica), mantendo seu histórico de saúde. | Cliente, Funcionário |

---

### Entidade Funcionário - US03 - Manter Funcionário
Um funcionário representa um usuário interno do sistema. Um funcionário tem: Nome, CPF, Cargo/Função, E-mail e Senha.

Requisito | Descrição | Ator |
--------- | ----------- | ---------- |
RF03.01 - Inserir Funcionário | Insere novo funcionário informando: Nome, CPF, Cargo/Função, E-mail e Senha. | Administrador |
RF03.02 - Listar Funcionários | Listagem dos funcionários e seus respectivos cargos. | Administrador |
RF03.03 - Atualizar Funcionário | Atualiza as informações de um funcionário, incluindo seu cargo e permissões. | Administrador |
RF03.04 - Desativar Funcionário | Desativa um funcionário, revogando seu acesso ao sistema. | Administrador |

---

### Entidade Produto - US04 - Manter Produto
Um produto é um item vendido no pet shop. Tem: Código, Nome, Descrição, Preço de Venda, Quantidade em Estoque, Categoria e Data de Validade.

Requisito | Descrição | Ator |
--------- | ----------- | ---------- |
RF04.01 - Inserir Produto | Insere novo produto informando: Código, Nome, Descrição, Preço, Estoque Inicial, Categoria e Data de Validade. | Administrador |
RF04.02 - Listar Produtos | Listagem de produtos com filtros por Nome, Categoria, Data de Validade, Preço. | Funcionário |
RF04.03 - Atualizar Produto | Atualiza as informações de um produto, incluindo o ajuste manual de estoque. | Administrador |
RF04.04 - Desativar Produto | Desativa um produto, impedindo novas vendas mas mantendo o histórico. | Administrador |

---

### Entidade Serviço - US05 - Manter Serviço
Um serviço representa os procedimentos oferecidos pela clínica. Tem: Nome, Descrição, Preço e Duração Estimada.

Requisito | Descrição | Ator |
--------- | ----------- | ---------- |
RF05.01 - Inserir Serviço | Insere novo serviço (ex: Banho e Tosa, Consulta) informando: Nome, Descrição, Preço e Duração. | Administrador |
RF05.02 - Listar Serviços | Listagem de todos os serviços oferecidos pela clínica. | Funcionário |
RF05.03 - Atualizar Serviço | Atualiza as informações de um serviço. | Administrador |
RF05.04 - Desativar Serviço | Desativa um serviço, impedindo novos agendamentos. | Administrador |

---

### Entidade Agendamento - US06 - Manter Agendamento
Um agendamento vincula um Cliente, um Pet, um Serviço e um horário na agenda da clínica.

Requisito | Descrição | Ator |
--------- | ----------- | ---------- |
RF06.01 - Agendar Serviço | Insere novo agendamento informando: Cliente, Pet, Serviço e Horário desejado. | Cliente, Funcionário |
RF06.02 - Listar Agendamentos | Listagem de agendamentos com filtros por data e status (confirmado, cancelado, concluído). | Funcionário, Administrador |
RF06.03 - Cancelar Agendamento | Altera o status de um agendamento para "Cancelado". | Cliente, Funcionário |
RF06.04 - Confirmar Serviço | Altera o status do agendamento para "Concluído" após a realização do serviço. | Funcionário |

---

### Entidade Venda - US07 - Realizar Venda
Uma venda registra a transação financeira de produtos e/ou serviços.

Requisito | Descrição | Ator |
--------- | ----------- | ---------- |
RF07.01 - Registrar Venda | Registra a venda de um ou mais produtos/serviços para um cliente, dando baixa no estoque. | Funcionário |
RF07.02 - Listar Vendas | Listagem do histórico de vendas com filtros por data e cliente. | Funcionário |
RF07.03 - Processar Pagamento | Registra o pagamento de uma venda, aceitando diferentes métodos como Pix e cartão. | Funcionário |
RF07.04 - Cancelar Venda | Cancela uma venda não finalizada, estornando os itens para o estoque. | Funcionário |

---

### Entidade Usuário - US08 - Autenticação
A autenticação controla o acesso seguro ao sistema.

Requisito | Descrição | Ator |
--------- | ----------- | ---------- |
RF08.01 - Login de Usuário | Realiza login no sistema informando credenciais (e-mail e senha). | Administrador, Funcionário, Cliente |
RF08.02 - Logout de Usuário | Realiza logout, encerrando a sessão do usuário de forma segura. | Administrador, Funcionário, Cliente |

---

### Entidade Relatório - US09 - Gerar Relatórios
O sistema deve ser capaz de gerar relatórios para auxiliar na tomada de decisão.

Requisito | Descrição | Ator |
--------- | ----------- | ---------- |
RF09.01 - Relatório Financeiro | Gera relatório de faturamento detalhado por período. | Administrador |
RF09.02 - Relatório de Vendas | Gera relatório dos produtos mais vendidos em um determinado período. | Administrador |
RF09.03 - Relatório de Estoque | Gera relatório de produtos com data de validade próxima ou com estoque baixo. | Administrador |
RF09.04 - Relatório de Clientes | Gera relatório de clientes ativos. | Administrador |