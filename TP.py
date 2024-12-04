import ply.lex as lex

# Liste des mots-clés
keywords = {
    'actor': 'ACTOR',
    'as': 'AS',
    'usecase': 'USECASE',
    'package': 'PACKAGE',
    'includes': 'INCLUDES',
    'extends': 'EXTENDS',
    '@startuml': 'STARTUML',
    '@enduml': 'ENDUML',
}

# Liste des tokens
tokens = [
    'COLON',          # :
    'RIGHT_ARROW_1',  # ->, -->, etc.
    'RIGHT_ARROW_2',  # .>, ..>, etc.
    'LBRACE',         # {
    'RBRACE',         # }
    'INHERIT',        # <|--
    'EOL',            # Fin de ligne
    'STRING',         # "chaine"
    'STEREO',         # <<superuser>>
    'ACTOR_TEXT',     # :Admin:
    'USE_CASE_TEXT',  # (Authentication)
    'ID',             # Identifiant comme user, start1, etc.
] + list(keywords.values())

# Règles de reconnaissance des tokens
t_COLON = r':'
t_RIGHT_ARROW_1 = r'->|-->'
t_RIGHT_ARROW_2 = r'\.>|\.\.>'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_INHERIT = r'<\|--'
t_STRING = r'"[^"]*"'
t_STEREO = r'<<[^>]+>>'
t_ACTOR_TEXT = r':[^:]+:'
t_USE_CASE_TEXT = r'[^)]*'

# Reconnaissance des identifiants (exclure les mots-clés)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'ID')  # Vérifie si c'est un mot-clé
    return t

# Ignorer les espaces et les tabulations
t_ignore = ' \t'

# Fin de ligne (EOL)
def t_EOL(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Gestion des erreurs lexicales
def t_error(t):
    print(f"Caractère non reconnu : {t.value[0]} à la ligne {t.lexer.lineno}")
    t.lexer.skip(1)

# Construire l'analyseur lexical
lexer = lex.lex()

# Exemple d'utilisation
if __name__ == "__main__":
    data = '''
    @startuml System
      actor :User:
      usecase (Define travel)
      :User: --> (Define travel)
    @enduml
    '''
    lexer.input(data)
    for token in lexer:
        print(token)