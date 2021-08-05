grammar = """

    // El axioma inicial
    ?start: exp+

    //Definicion de una expresion
    ?exp: "siuu" var "=" string "$" -> assignvar
        | "siuu" var "=" arithmeticoperation "$" -> assignvar
        | "pantalla" string "$" -> print
        | "pantalla" var "$" -> printvar

    // Definicion de operacion aritmetica
    ?arithmeticoperation: product
        | arithmeticoperation "+" product -> add
        | arithmeticoperation "-" product -> sub
    
    ?product: atom
        | product "*" atom -> mul
        | product "/" atom -> div

    ?atom: var -> getvar
        | number
        | "-" atom
        | "(" atom ")"

    ?string: /'[^']*'/
        
    ?var: /[a-zA-Z]\w*/

    ?number: /\d+(\.\d+)?/

    %ignore /\s+/
"""
