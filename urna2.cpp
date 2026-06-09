#include <iostream>
#include <vector>
using namespace std;

// Variaveis Globais
vector<string> nomeCandidatos = {
    "Maria",
    "Jose",
    "Joao",
    "Pedro",
    "Julia",
};
vector<int> votosCandidatos = {0, 0, 0, 0, 0};
vector<int> maisVotados = {};
bool segundoTurno = false;
int totalVotos = 0;

// Metodos

void espera()
{
    cin.ignore();
    cin.get(); // para dar tempo pro usuario ler a lista.
}

int menuPrincipal()
{
    int opcaoMenuPrincipal;
    system("cls");
    while (true)
    {
        cout << "Menu: \n";
        cout << "1-Cadastrar Candidatos \n";
        cout << "2-Iniciar Votacao \n";
        cout << "Escolha a opcao: ";
        cin >> opcaoMenuPrincipal;

        if (opcaoMenuPrincipal == 1)
        {
            return 1;
            break;
        }
        else if (opcaoMenuPrincipal == 2)
        {
            return 2;
            break;
        }
        else
        {
            cout << "Nao existe essa opcao, tente novamente.\n";
        }
    }
}

void menuLista(int votOUlist)
{
    system("cls");
    cout << "Lista de Candidatos: \n";
    if (votOUlist == 1)
    {
        cout << "0-Mostrar resultado \n";
    }
    for (int i = 0; i < nomeCandidatos.size(); i++)
    {

        cout << i + 1 << "-" << nomeCandidatos[i] << endl;
    }
}

void cadastrar()
{
    char opcaoCadastrar;
    string addCandidato;
    cout << " Deseja Cadastrar um candidato (s/n)? ";
    cin >> opcaoCadastrar;
    cin.ignore();
    if (opcaoCadastrar == 's')
    {
        cout << "Adicione o candidato aqui: ";
        getline(cin, addCandidato);
        nomeCandidatos.push_back(addCandidato);
        votosCandidatos.push_back(0);
        cout << "Cadastro Salvo ";
    }
}

void excluir()
{
    int opcaoExcluir;
    char confirmacaoExcluir;
    menuLista(2);
    cout << "Escolha um candidato para ser excluido: ";
    cin >> opcaoExcluir;
    if (opcaoExcluir <= votosCandidatos.size() && opcaoExcluir > 0)
    {
        cout << "Voce tem certeza que deseja excluir o candidado " << nomeCandidatos[opcaoExcluir - 1] << " (s/n)? ";
        cin >> confirmacaoExcluir;
        if (confirmacaoExcluir == 's' && opcaoExcluir <= votosCandidatos.size() && opcaoExcluir > 0)
        {
            nomeCandidatos.erase(nomeCandidatos.begin() + opcaoExcluir - 1);
            votosCandidatos.erase(votosCandidatos.begin() + opcaoExcluir - 1);
        }
    }
    else
    {
        cout << " Opcao invalida \n";
        cout << "Aperte enter para continuar";
        espera();
    }
}

int menuCadastro()
{
    int opcaoCadastro;
    while (true)
    {
        system("cls");
        cout << "Menu Cadastro: \n";
        cout << "0-Voltar \n";
        cout << "1-Cadastrar \n";
        cout << "2-Excluir \n";
        cout << "3-Listar \n";
        cout << "Escolha a opcao: ";
        cin >> opcaoCadastro;
        if (opcaoCadastro == 0)
        {
            return 0;
        }
        else if (opcaoCadastro == 1)
        {
            cadastrar();
        }
        else if (opcaoCadastro == 2)
        {
            excluir();
        }
        else if (opcaoCadastro == 3)
        {
            menuLista(2);
            cout << "Aperte enter para sair da lista.";
            espera();
        }
    }
}

vector<int> listaGanhadores(vector<int> &listaCandidado)
{
    int maiorVoto = 0;
    vector<int> classificados = {};
    for (int i = 0; i < listaCandidado.size(); i++)
    {
        if (listaCandidado[i] > maiorVoto)
        {
            maiorVoto = listaCandidado[i];
        }
    }
    for (int i = 0; i < listaCandidado.size(); i++)
    {
        if (listaCandidado[i] == maiorVoto)
        {
            classificados.insert(classificados.end(), i);
        }
    }
    return classificados;
}

bool resultado(vector<int> &listaQuantidadeVotos, vector<string> &listaNomes)
{

    system("cls");
    cout << "Resultados da Votacao \n";
    maisVotados = listaGanhadores(listaQuantidadeVotos);

    cout << "Total de Votos -> " << totalVotos << endl;
    for (int i = 0; i < listaNomes.size(); i++)
    {

        cout << i + 1 << "-" << listaNomes[i] << "-> " << listaQuantidadeVotos[i] << endl;
    }

    if (maisVotados.size() > 1)
    {
        segundoTurno = true;
        return true;
    }
    else
    {
        segundoTurno = false;
        cout << "Vencedor e: " << listaNomes[maisVotados[0]] << " com " << listaQuantidadeVotos[maisVotados[0]] << " votos";
        espera();
        return false;
    }
}

bool votacao(vector<int> &listaQuantidadeVotos, vector<string> &listaNomes)
{
    string senha;
    cout << "Escolha seu Candidato: ";
    int voto;
    cin >> voto;
    if (voto == 0)
    {
        system("cls");
        cout << "(senha = senhateste123)\nDigite a senha: ";
        cin >> senha;
        if (senha == "senhateste123")
        {
            return resultado(listaQuantidadeVotos, listaNomes);
        }
        else
        {
            cout << "Senha invadila.\n";
            cout << "Aperte enter para tentar novamente.";
            espera();
            return true;
        }
    }
    else if (voto > listaQuantidadeVotos.size() || voto < 0)
    {
        cout << "Candidalido Invalido \n";
        cout << "Aperte Enter.";
        espera();

        return true;
    }
    else
    {
        listaQuantidadeVotos[voto - 1]++;
        totalVotos++;
        return true;
    }
}

vector<string> turnoII(vector<int> &listaDeCandidatos)
{
    cout << "Escolha seu Candidato: \n";
    vector<string> nomes = {};
    cout << "0-Mostrar resultado \n";
    for (int i = 0; i < listaDeCandidatos.size(); i++)
    {
        nomes.push_back(nomeCandidatos[listaDeCandidatos[i]]);
        cout << i + 1 << "-" << nomeCandidatos[listaDeCandidatos[i]] << endl;
    }
    return nomes;
}

void reseteVotacao(vector<int> &listaReset)
{
    totalVotos = 0;
    for (size_t i = 0; i < listaReset.size(); i++)
    {
        listaReset[i] = 0;
        // cout << votosCandidatos[i] <<endl;
    }
}

// urna

int main()
{
    bool primeiroTurno = true;

    int opcaoMain = menuPrincipal();

    if (opcaoMain == 1)
    {
        int opcaoCadastro = menuCadastro();
        if (opcaoCadastro == 0)
        {
            main();
        }
    }
    else if (opcaoMain == 2)
    {
        while (primeiroTurno)
        {
            menuLista(1);

            primeiroTurno = votacao(votosCandidatos, nomeCandidatos);

            if (segundoTurno)
            {
                system("cls");
                reseteVotacao(votosCandidatos);
                cout << " Ocorreu um empate. \n";
                cout << " Segundo Turno: \n";
                while (segundoTurno)
                {
                    system("cls");
                    vector<string> nomes = turnoII(maisVotados);

                    votacao(votosCandidatos, nomes);
                }
                break;
            }
            else if (maisVotados.size() == 1)
            {
                break;
            }
        }
    }
}
