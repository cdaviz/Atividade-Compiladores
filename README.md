Relatório 

Este trabalho consiste na implementação de um analisador léxico para a linguagem C utilizando a biblioteca PLY (Python Lex-Yacc). O analisador tem como objetivo reconhecer e categorizar os elementos da linguagem, como palavras-chave, identificadores, operadores e delimitadores.
O programa foi desenvolvido utilizando PLY para realizar a tokenização do código-fonte escrito em C. O funcionamento segue as etapas:
Definição dos Tokens: Listagem dos elementos léxicos reconhecidos, como palavras-chave (ex: if, while), operadores (+, -, ==), identificadores e números.
Expressões Regulares: Cada token é identificado por meio de padrões regex, permitindo o reconhecimento de estruturas sintáticas específicas.
Ignoração de Espaços e Comentários: O lexer descarta espaços em branco e comentários (// e /* ... */).
Tratamento de Erros: Caracteres inválidos geram mensagens de erro para auxiliar na depuração.
Processamento da Entrada: O código-fonte é lido e processado, gerando uma lista de tokens como saída.


Entrada (código C)

int main() {
    int x = 10;
    float y = 20.5;
    if (x < y) {
        x = x + 1;
    }
    return 0;
}

Saída Gerada pelo Lexer

Token(INT, 'int')

Token(ID, 'main')

Token(LPAREN, '(')

Token(RPAREN, ')')

Token(LBRACE, '{')

Token(INT, 'int')

Token(ID, 'x')

Token(ASSIGN, '=')

Token(NUMBER, '10')

Token(SEMI, ';')

Token(FLOAT, 'float')

Token(ID, 'y')

Token(ASSIGN, '=')

Token(NUMBER, '20.5')

Token(SEMI, ';')

Token(IF, 'if')

Token(LPAREN, '(')

Token(ID, 'x')

Token(LT, '<')

Token(ID, 'y')

Token(RPAREN, ')')

Token(LBRACE, '{')

Token(ID, 'x')

Token(ASSIGN, '=')

Token(ID, 'x')

Token(PLUS, '+')

Token(NUMBER, '1')

Token(SEMI, ';')

Token(RBRACE, '}')

Token(RETURN, 'return')

Token(NUMBER, '0')

Token(SEMI, ';')

Token(RBRACE, '}')

Dificuldades:

Reconhecimento correto de operadores compostos (==, <=, >=, !=). Inicialmente, os operadores simples estavam sendo reconhecidos antes dos compostos.

Ignoração de Comentários: O tratamento de comentários de múltiplas linhas exigiu ajustes na expressão regular para lidar corretamente com espaços e novas linhas.

Detecção de Erros: Implementar um mecanismo para exibir mensagens de erro ao encontrar caracteres desconhecidos.

As próximas etapas de um compilador:

Análise Semântica: Verificação de tipos e declarações de variáveis.

Geração de Código Intermediário: Conversão do código-fonte para uma representação intermediária antes da compilação final.

Otimização de Código: Melhoria no desempenho do código gerado.

Geração de Código Final: Transformação para código de máquina ou bytecode.
