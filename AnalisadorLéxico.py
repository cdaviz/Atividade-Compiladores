import ply.lex as lex

# Lista de tokens
tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA',
    'EQ', 'LT', 'GT',  # Operadores de comparação
    'IF', 'ELSE', 'WHILE', 'FOR', 'RETURN', 'INT', 'FLOAT', 'VOID'
)

# Palavras-chave de C
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'return': 'RETURN',
    'int': 'INT',
    'float': 'FLOAT',
    'void': 'VOID'
}

# Expressões regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'
t_COMMA   = r','

# Operadores relacionais
t_EQ = r'=='
t_LT = r'<'
t_GT = r'>'

# Variável global para contar erros
error_found = False

# Regra para números (inteiros e floats)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Regra para identificadores e palavras-chave
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é palavra-chave
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Comentários em C (de linha e de bloco)
def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    pass  # Ignorar comentário

# Regra para reconhecer novas linhas e atualizar a contagem de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erro para caracteres inválidos
def t_error(t):
    global error_found
    error_found = True
    print(f"Erro léxico: Caractere inválido '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Teste do lexer
if __name__ == "__main__":
    data = '''
        int main() {
        int x = 10;
        float y = 20.5;
        if (x > y) {  
            x = x + 1;
        }
        else (x == y) {  
            return 1;
        }
        return 0;
    }
    '''
    
    lexer.input(data)
    
    for tok in lexer:
        print(tok)

    # Verificação final de erros
    if error_found:
        print("\nAnálise léxica finalizada: ERROS encontrados!")
    else:
        print("\nAnálise léxica finalizada: Nenhum erro encontrado.")
