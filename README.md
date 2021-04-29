# TPW_Trabalho1 - Football Nerds.

João Soares Nmec 93078

Hugo Ferreira Nmec 93093

### Practical Work 1 - Foorball Nerds

### Link:
 >**http://joaots.pythonanywhere.com/**

## GitHub Repository:
 >**https://github.com/JoaoTS20/TPW_Trabalho1**

## Description

- *Football Nerds.* is a Website with Data related to the Football World


## Contas
- *Admin* Account:
  - username: admin
  - password: admin1234

  
- *NormalUser* Account:
  - username: user1
  - password: 3=eX6xXK
  
## Funcionalidades e Autorizações


### Sign Up/Login

- **NoLogin:**
    - Poderá realizar Sign Up apenas de NormalUser
        - É pedido username, email adress, Password
        - Deverá ainda indicar se tem um trabalho ligado à área do Futebol
        - Caso insira dados incorretos serão apresentadas mensagens de erro

- ***NormalUser:*** 
  - Pode realizar  Login

- **Admin:**
   - Pode realizar Login

### Adicionar Comentários
- **NoLogin:**
   - Não pode adicionar comentários na Página_Detalhada de ***Competitions/Teams/Players/Staff***.
- **NormalUser:**
   - Pode adicionar comentários na Página_Detalhada de ***Competitions/Teams/Players/Staff***.
- **Admin:**
   - Não pode adicionar comentários na Página_Detalhada de ***Competitions/Teams/Players/Staff***.

### Adicionar/Remover Favoritos
- **NoLogin:**
   - Não pode adicionar/remover Favoritos.
  
- ***NormalUser*** 
  - Pode adicionar e posteriormente remover ***Competitions/Teams/Players/Staff*** como Favoritos e visualizar a lista dos mesmos no seu profile */profile*.

- **Admin:**
   - Não pode adicionar/remover Favoritos.

### Pesquisa Filtrada:
- ***NormalUser/Admin/NoLogin*** podem pesquisar ***Teams/Competitions/Players/Staff*** por diferentes parâmetros ao mesmo tempo:
  - **Team**
    - Search By:
      - Name
      - Country
      - Competition
    - Order By:
      - Founding Year
      - Full Name
    
  - **Competition**
    - Search By:
      - Name
      - Region
    - Order By:
      - Region
      - Full Name
  
  - **Team**
    - Search By:
      - Name
      - Nationality
      - Position
      - Best Foot
    - Order By:
      - BirthDay
      - Full Name
      - Height
  
***Para reiniciar a pesquisa simplesmente pesquise com parametros vazios.***

### Visualizar Dados em Detalhe:
- **NoLogin/NormalUser/Admin**:
  - Pode Visualizar:
    - **Competition:** Pode Visualizar Comentários, Dados sobre a Competition  e por época as Teams que participam e Matches da Competition que permitem gerar a Tabela Classificativa.
    - **Team:** Pode Visualizar Comentários, Dados sobre a Team e por época os Players da Team, o Staff da Team e as Competitions que participam.
    - **Player:** Pode Visualizar Comentários, Dados sobre o Player e as Teams que o Player jogou em determinada época.
    - **Staff:** Pode Visualizar Comentários, Dados sobre o Staff e as Teams que o Staff "participou" em determinada época.
  


***Por Default sem selecionar uma época os dados expostos são sobre a atual época 2020-2021***

### Inserir Dados
  - **NoLogin:**
      - Não pode Inserir Dados
  - **NormalUser:**
    - Pode apenas Inserir ***Team/Staff/Player/Competition***
  - **Admin:**
    - Pode Inserir ***Team/Staff/Player/Competition***
    - Pode Inserir relações entre as entidades ***Team/Staff/Player/Competition***:
      - Team joga numa Competition em determinada época (*ClubPlaysIn*)
      - Player joga numa Team em determinada época (*StaffManages*)
      - Staff trabalha numa Team em determinada época (*PlayerPlaysFor*)
    - Pode Inserir as Matches de uma Competition:
      - (*Match*) e (*CompetitionsMatches*) realizada de forma simultânea
  
### Editar Dados
  - **NoLogin:**
      - Não pode Editar Dados
  - **NormalUser:**
    - Não pode Editar Dados  
  - **Admin:**
    - Pode Editar ***Team/Staff/Player/Competition***
  
### Eliminar Dados
  - **NoLogin:**
      - Não pode Eliminar Dados
  - **NormalUser:**
    - Não pode Eliminar Dados  
  - **Admin:**
    - Pode Eliminar ***Team/Staff/Player/Competition*** e consequentemente as suas Relações.
  
    
## URLs
    competitions/ 
    competitions/<int:id>
    competitions/<int:id>/<str:season>
    insertcompetition/
    editcompetition/<int:id>/
    insertteamincompetition/<int:compid>/<str:season>/

    teams/
    teams/<int:id>
    teams/<int:id>/<str:season>
    insertteam/
    editteam/<int:id>/
    insertplayerinteam/<int:teamid>/

    players/
    players/<int:id>
    insertplayer/
    editplayer/<int:id>/

    staff/
    staff/<int:id>
    insertstaff/
    editstaff/<int:id>/
    insertstaffinteam/<int:teamid>/

    match/<int:id>
    insertmatch/
    insertmatch/<int:compid>

    login/
    logout/
    signup/
    profile/

-  Inserido um URL incorreto ou sem autorização para o aceder é redirecionado para uma página de erro
## Requirements
- `Python 3.8 / 3.9`

- `Django 3.2`

- `Pillow 2.8.0`

- `pip 20.2.3`

